<script>
	import favicon from '$lib/assets/favicon.svg';
  	import Header from '$lib/components/header.svelte';
</script>

<svelte:head>
<<<<<<< HEAD
	<link rel="icon" type="image/png" href={favicon} />
=======
  <link rel="icon" href={favicon} />
>>>>>>> 778d8e401b9dcc6c0a09a0f96c0537b593676b5e
</svelte:head>

<Header />

<slot />
<style global>
  @import '../app.css';
</style>