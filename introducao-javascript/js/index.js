function createPacienteFromForm(form) {
	return {
		nome: form.nome.value,
		peso: form.peso.value,
		altura: form.altura.value,
		gordura: form.gordura.value,
		imc: calcularIMC(form.peso.value, form.altura.value),
		getErros: function () {
			var erros = [];

			if (this.peso < 0 || this.peso > 100) {
				erros.push("Peso Inválido");
			}

			if (this.altura < 0 || this.altura > 3.00) {
				erros.push("Altura Inválida");
			}

			return erros;
		}
	}
}

function createTd(dado, classe) {
	var newTd = document.createElement('td');

	newTd.textContent = dado;
	newTd.className = classe;

	return newTd;
}

function createTr(paciente) {
	var newTr = document.createElement('tr');

	newTr.appendChild(createTd(paciente.nome, 'info-nome'));
	newTr.appendChild(createTd(paciente.peso, 'info-peso'));
	newTr.appendChild(createTd(paciente.altura, 'info-altura'));
	newTr.appendChild(createTd(paciente.gordura, 'info-gordura'));
	newTr.appendChild(createTd(paciente.imc.toFixed(2), 'info-imc'));

	return newTr;
}

function atualizarErros(erros) {
	var errorList = document.querySelector("#error-list");

	errorList.innerHTML = "";

	if (erros.length > 0) {
		erros.forEach(function(erro) {
			var li = document.createElement('li');
			li.textContent = erro;
			errorList.appendChild(li); 
		});
	}
}


var titulo = document.querySelector(".titulo");
titulo.textContent = "Aparecida Nutricionista";

var botaoAdicionar = document.querySelector('#adicionar-paciente');

botaoAdicionar.addEventListener("click", function (event) {
	event.preventDefault();
	var formulario = document.querySelector('#form-cadastro');
	var paciente = createPacienteFromForm(formulario);
	
	erros = paciente.getErros();
	atualizarErros(erros);
	if (erros.length > 0) {
		return;
	}

	var trPaciente = createTr(paciente);
	tbPacientes = document.querySelector('#tabela-pacientes');
	tbPacientes.appendChild(trPaciente);
	formulario.reset();
});
