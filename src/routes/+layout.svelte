<script>
	import favicon from '$lib/assets/favicon.svg';
  	import Header from '$lib/components/header.svelte';
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<Header />
<slot />