<script>
	import favicon from '$lib/assets/favicon.svg';
  	import Header from '$lib/components/header.svelte';
</script>
<div class="abstract-top"></div>
<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<Header />

<slot />
<style global>
  @import '../app.css';
</style>