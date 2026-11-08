from pathlib import Path

source_path = Path("/mnt/data/Pasted text(3).txt")
output_path = Path("/mnt/data/app.py")

code = source_path.read_text(encoding="utf-8")

# Ensure the reported navigation condition is a single, properly closed string.
code = code.replace(
    'elif selected_module == "🧠 Dialogue with\n the Void (AI Interrogator)":',
    'elif selected_module == "🧠 Dialogue with the Void (AI Interrogator)":'
)
code = code.replace(
    'elif selected_module == "🧠 Dialogue with\n',
    'elif selected_module == "🧠 Dialogue with the Void (AI Interrogator)":\n'
)

# Validate the complete file before writing it.
compile(code, str(output_path), "exec")
output_path.write_text(code, encoding="utf-8")

print(f"Syntax yoxlaması uğurludur. Fayl yaradıldı: {output_path}")
