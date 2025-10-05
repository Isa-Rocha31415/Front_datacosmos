<script>
	import favicon from '$lib/assets/favicon.svg';
  	import Header from '$lib/components/header.svelte';
</script>

<svelte:head>
	<link rel="icon" type="image/png" href={favicon} />
</svelte:head>

<Header />

<slot />
<style global>
  @import '../app.css';
</style>