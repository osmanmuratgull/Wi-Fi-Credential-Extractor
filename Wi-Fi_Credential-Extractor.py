import subprocess

# Execute cmd command and capture output
result = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True, encoding='latin-1')

# Extract Wi-Fi credentials from the command output
wifi_credentials = []
for line in result.stdout.splitlines():
    if line.startswith("SSID name") or line.startswith("Key Content"):
        _, _, value = line.partition(":")
        wifi_credentials.append(value.strip())

# Write the Wi-Fi credentials to the output file
with open("passwords.txt", "w") as f:
    f.write("Available Wi-Fi credentials on the machine:\n\n")
    for i in range(0, len(wifi_credentials), 2):
        ssid = wifi_credentials[i]
        password = wifi_credentials[i + 1]
        f.write(f"[*] SSID: {ssid}\n[!] Password: {password}\n\n")
