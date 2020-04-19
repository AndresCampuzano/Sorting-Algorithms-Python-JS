function bubbleSort(array) {
	const n = array.length;
	let aux = 0;
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n - i - 1; j++) {
			if (array[j] > array[j + 1]) {
				aux = array[j];
				array[j] = array[j + 1];
				array[j + 1] = aux;
			}
		}
	}
	console.log(array);
}

bubbleSort([190, 1200, 1, 2, 4, 55, 1000, 6, 800, -56, 0, 8]);
