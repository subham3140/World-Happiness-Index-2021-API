$('.btn1').on("click", () => {
    $('.modalbtn1')[0].click();
})

$('.searchbycountry').on('click', () => {
    let countryname = $('#countryname')[0].value;
    window.location.href = window.location.href + "v1/country?country=" + countryname;
})