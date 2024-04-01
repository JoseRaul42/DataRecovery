import os
import itertools
import sys
import time
import threading

def get_byte_sequences(mimetype):
    sequences = {
        "jpg": (b'\xff\xd8\xff\xe0\x00\x10\x4a\x46', b'\xff\xd9'),
        "png": (b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a', b'\x49\x45\x4e\x44\xae\x42\x60\x82'),
        "pdf": (b'%PDF-', b'%%EOF'),
    }
    return sequences.get(mimetype, (b'START_BYTES', b'END_BYTES'))

def loading_animation(event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if event.is_set():
            break
        sys.stdout.write('\r' + c + ' Scanning...')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!          \n')


def recover_files(bytes_size, mimetype, source_drive, destination_directory, drive_letter):
    start_seq, end_seq = get_byte_sequences(mimetype)
    stop_event = threading.Event()
    animation_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    print("This may take a while, depending on the size of the drive and the number of recoverable files.")
    animation_thread.start()
    
    try:
        drive = f"\\\\.\\{drive_letter}:"
        with open(drive, "rb") as fileD:
            byte = fileD.read(bytes_size)
            offs = 0
            drec = False
            rcvd = 0
            
            while byte:
                found = byte.find(start_seq)
                if found >= 0:
                    drec = True
                    recovered_file_path = os.path.join(destination_directory, f"{rcvd}.{mimetype.split('/')[-1]}")
                    print(f"==== Found {mimetype} at location: {hex(found + (bytes_size * offs))} ====")
                    with open(recovered_file_path, "wb") as fileN:
                        fileN.write(byte[found:])
                        while drec:
                            byte = fileD.read(bytes_size)
                            bfind = byte.find(end_seq)
                            if bfind >= 0:
                                fileN.write(byte[:bfind + 2])
                                print(f"==== Wrote {mimetype} to location: {recovered_file_path} ====\n")
                                drec = False
                                rcvd += 1
                            else:
                                fileN.write(byte)
                byte = fileD.read(bytes_size)
                offs += 1
        print("Recovery operation completed.")
    except IOError as e:
        print(f"Failed to access drive or write file. Error: {e}")
