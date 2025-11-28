def transform_poe_chat(text: str) -> str:
    lines = text.splitlines()
    output = []
    in_user_block = False
    # Buffer to hold empty lines so we can decide whether to quote them or not
    # depending on what comes next (more text vs. Assistant block)
    pending_empty_lines = 0

    for line in lines:
        stripped = line.strip()

        # Check for User block start
        if stripped == "User:":
            in_user_block = True
            output.append("> [!note]")
            pending_empty_lines = 0
            continue

        # Check for Assistant block start (ends User block)
        if stripped == "Assistant:":
            in_user_block = False
            # Flush any pending empty lines as clean newlines (no quotes)
            # because they are just separators before the Assistant
            output.extend([""] * pending_empty_lines)
            pending_empty_lines = 0
            output.append(line)
            continue

        # Handle content inside User block
        if in_user_block:
            if stripped == "":
                # Buffer empty lines, don't print yet
                pending_empty_lines += 1
            else:
                # We hit text.
                # 1. Flush any buffered empty lines AS QUOTED lines
                #    because they are clearly part of the user's message body.
                for _ in range(pending_empty_lines):
                    output.append(">")
                pending_empty_lines = 0

                # 2. Print the current line quoted
                output.append(f"> {line}")
        else:
            # Handle content outside User block (Assistant or other)
            output.append(line)

    # Flush any remaining empty lines at the very end of the file
    # If we are still in user block, typically we don't quote trailing whitespace
    if pending_empty_lines > 0:
        output.extend([""] * pending_empty_lines)

    return "\n".join(output)
