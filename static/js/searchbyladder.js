$('.btn2').on("click", () => {
    $('.modalbtn2')[0].click();
})

$('.searchbyladder').on('click', () => {
    let ladderfrom = $('#ladderfrom')[0].value;
    let ladderto = $('#ladderto')[0].value;
    window.location.href = window.location.href + "v1/score-range?from=" + ladderfrom + "&to=" + ladderto;
})