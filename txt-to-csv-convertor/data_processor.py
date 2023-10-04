import re

def process_lines(lines):
    data = []
    last_known_password = "N/A"
    i = 0

    # Regex pattern to match variations of 'password'
    password_pattern = re.compile(r'pass(?:w[o0]rd?)?\s*:? ?(.+)', re.I)

    while i < len(lines):
        line = lines[i].strip()

        # Handle various password formats using regex
        match = password_pattern.search(line)
        if match:
            last_known_password = match.group(1).strip()  # Extract password
            if last_known_password.lower() in ["password", "passwd", "pwd"]:
                # Replace with next longest part (if available)
                parts = line.split()
                filtered_parts = [part for part in parts if part.lower() not in ["password", "passwd", "pwd"]]
                if filtered_parts:
                    last_known_password = max(filtered_parts, key=len)
                    
            i += 1
            continue

        # Collect ID and Codes, considering multiple newlines
        id_line, codes = None, []
        while i < len(lines):
            line = lines[i].strip()

            if line.isdigit():
                if id_line is None:
                    id_line = line  # Assign ID if not already assigned
                else:
                    codes.append(line)  # Else, consider it a code
            elif any(word in line.lower() for word in ["password", "passwd", "pwd"]):
                break  # Stop if a new password line is encountered, to avoid mixing data
            elif line == "":  # Skip empty lines
                i += 1
                continue
            else:
                break  # Stop if a line doesn't meet any condition

            i += 1

        if id_line and codes:  # Ensure we have both ID and codes to write
            data.append([id_line, last_known_password, ",".join(codes)])

    return data
