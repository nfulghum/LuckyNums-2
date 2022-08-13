/** processForm: get data from form and make AJAX call to our API. */
const BASE_URL = "http://127.0.0.1:5000"

async function processForm(evt) {
    evt.preventDefault();
    $('#name-err, #email-err, #year-err, #color-err').empty();

    let name = $('#name').val();
    let email = $('#email').val();
    let year = $('#year').val();
    let color = $('#color').val();

    const newUserResponse = await axios.post(`${BASE_URL}/api/get-lucky-num`, {
        name, email, year, color
    });

    let res = newUserResponse.data
    handleResponse(res);

    return;
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    $('#lucky-results').empty();

    $('#lucky-results').append(
        `<p>Your lucky number is ${resp.num['num']} (Fun fact: ${resp.num['fact']})</p>`
    );

    $('#lucky-results').append(
        `<p>Your birth year is ${resp.year['year']} (Fun fact: ${resp.year['fact']})</p>`
    );

    $('#lucky-form').trigger('reset');
}


$("#lucky-form").on("submit", processForm);
