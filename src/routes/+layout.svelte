<script>
<<<<<<< HEAD
// @ts-nocheck

	import favicon from '$lib/assets/favicon.svg';
    import Header from '$lib/components/header.svelte';
=======
	import favicon from '$lib/assets/favicon.svg';
  	import Header from '$lib/components/header.svelte';
>>>>>>> 778d8e401b9dcc6c0a09a0f96c0537b593676b5e
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<Header />

<slot />
<style global>
  @import '../app.css';
</style>