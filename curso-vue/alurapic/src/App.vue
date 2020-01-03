<template>
	<div>
		<h1> {{ titulo }} </h1>
		<ul>
			<li v-for="foto in fotos">
				<img :src="foto.url" :title="foto.titulo">
			</li>
		</ul>
	</div>
</template>

<script>
export default {

	data() {
		return {
			titulo: 'Alurapic',
			fotos: []
		};
	},

	created() {
		this.$http.get('http://localhost:3000/v1/fotos')
			.then(response => response.json())
			.then(fotos => this.fotos = fotos)
		;
	}

}
</script>

<style>

</style>
