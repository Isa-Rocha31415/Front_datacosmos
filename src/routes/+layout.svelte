<script>
	import icon from '$lib/assets/icon.png';
  	import Header from '$lib/components/header.svelte';
</script>
<div class="abstract-top"></div>
<svelte:head>
  <link rel="icon" href={icon} />
</svelte:head>


<Header />

<slot />
<style global>
  @import '../app.css';
</style>