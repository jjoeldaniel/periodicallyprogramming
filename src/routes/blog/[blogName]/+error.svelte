<script>
	import { page } from '$app/stores';
	import { ProgressRadial } from '@skeletonlabs/skeleton';
</script>

<div class="container h-full space-y-10 mx-auto max-w-xl flex flex-col justify-center items-center">
	<div class="flex flex-row">
		<h1>{$page.error.message}</h1>
		<ProgressRadial />
	</div>

	<div>
		<h5>Redirecting you back home...</h5>
	</div>
</div>
