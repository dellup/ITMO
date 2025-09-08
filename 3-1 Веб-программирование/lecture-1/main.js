const btn = document.getElementById("bt");
const result1 = document.getElementById("result1");
const result2 = document.getElementById("result2");

btn.addEventListener("click", () => {
    const a1 = Number(document.getElementById("n1").value);
    const b1 = Number(document.getElementById("n2").value);
    const c1 = Number(document.getElementById("n3").value);
    const a2 = Number(document.getElementById("n4").value);
    const b2 = Number(document.getElementById("n5").value);
    const c2 = Number(document.getElementById("n6").value);

    const b3 = a1 * b2 - a2 * b1;
    const e1 = c1 * b2 - b1 * c2;
    const e2 = a1 * c2 - a2 * c1;

    const x = e1 / b3;
    const y = e2 / b3;

    result1.value = x;
    result2.value = y;
});
