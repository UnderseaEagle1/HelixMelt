function tn_calc(primer, num_changed_bases) {
    let filtered = primer.toLowerCase().replace(/\s/g, "");

    if (filtered.length === 0) {
        return "Error: Primer is empty";
    }
    if (!/^[atcg]+$/.test(filtered)) {
        return "Error: Primer must contain only A, T, C, or G";
    }

    let percent_mismatch = (num_changed_bases / filtered.length) * 100;

    let gc_count = (filtered.match(/[gc]/g) || []).length;
    let percent_gc = (gc_count / filtered.length) * 100;

    let tn_value = 81.5 + (0.41 * percent_gc) - (675 / filtered.length) - percent_mismatch;

    return `Percent GC: ${percent_gc.toFixed(2)}%\nTn: ${tn_value.toFixed(2)}°C`;
}


function runCalculation() {
    let primer = document.getElementById("primer").value;
    let changes = document.getElementById("changes").value;

    let output = document.getElementById("output");

    if (isNaN(changes) || changes === "") {
        output.innerText = "Error: Changed bases must be an integer.";
        return;
    }

    let tn = tn_calc(primer, parseInt(changes));
    output.innerText = tn;
}
