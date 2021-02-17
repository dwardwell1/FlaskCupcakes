BASE_URL = 'http://127.0.0.1:5000/api';

function createCakesHTML(cake) {
	return `
    <div data-cupcake-id=${cake.id}>
     <li>
     ${cake.flavor} | ${cake.size} | ${cake.rating}
     </li>
     <img class="cake-img" src="${cake.image}"
     </div>
    `;
}
async function getCakeInfo() {
	let response = await axios.get(`${BASE_URL}/cupcakes`);

	for (let cakedata of response.data.cupcakes) {
		let newcake = $(createCakesHTML(cakedata));
		$('#cupcakes_list').append(newcake);
	}
}

/** handle form for adding of new cupcakes */

$('#new-cupcake-form').on('submit', async function(evt) {
	evt.preventDefault();

	let flavor = $('#flavor').val();
	let rating = $('#rating').val();
	let size = $('#size').val();
	let image = $('#image').val();

	const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
		flavor,
		rating,
		size,
		image
	});

	let newCupcake = $(createCakesHTML(newCupcakeResponse.data.cupcake));
	$('#cupcakes_list').append(newCupcake);
	$('#new-cupcake-form').trigger('reset');
});

getCakeInfo();
