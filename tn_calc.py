import tkinter as tk
from tkinter import messagebox

# --- Your functions (slightly modified for GUI output) ---

def tn_calc(primer, num_changed_bases):
    filtered_primer = primer.lower().replace(" ", "")
    
    if len(filtered_primer) == 0:
        return "Error: Primer is empty"

    percent_mismatch = (num_changed_bases / len(filtered_primer)) * 100
    percent_gc = ((filtered_primer.count('g') + filtered_primer.count('c')) / len(filtered_primer)) * 100

    tn_value = 81.5 + (.41 * percent_gc) - (675 / len(filtered_primer)) - percent_mismatch

    return f"Percent GC: {percent_gc:.2f}%\nTn Value: {tn_value:.2f}"


def out_primer(primer):
    nucleotide_dict = {'a':'t', 't':'a', 'g':'c', 'c':'g'}

    filtered_primer = primer.lower().replace(" ", "")
    
    try:
        complement_primer = ''.join([nucleotide_dict[char] for char in filtered_primer])
    except KeyError:
        return "Error: Primer contains invalid characters (only A, T, G, C allowed)"

    output = (
        f"3' {filtered_primer.lower()} 5'\n"
        f"3' {complement_primer[::-1]} 5'"   
        )

    return output


# --- GUI Function ---

def run_calculations():
    primer = primer_entry.get()
    try:
        num_changes = int(changes_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Number of changed bases must be an integer.")
        return

    tn_result = tn_calc(primer, num_changes)
    primer_result = out_primer(primer)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, tn_result + "\n\n"  + primer_result)


# --- Tkinter Window Setup ---

root = tk.Tk()
root.title("Primer Analysis Tool")
root.geometry("500x400")

# Primer input
tk.Label(root, text="Enter Primer Sequence:").pack(pady=5)
primer_entry = tk.Entry(root, width=50)
primer_entry.pack(pady=5)

# Number of changes input
tk.Label(root, text="Number of Changed Bases:").pack(pady=5)
changes_entry = tk.Entry(root, width=20)
changes_entry.pack(pady=5)

# Run button
tk.Button(root, text="Calculate", command=run_calculations).pack(pady=10)

# Output box
output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=10)

# Run app
root.mainloop()