<script lang="ts">
	import { page } from '$app/stores';
	import { ProgressRadial } from '@skeletonlabs/skeleton';

	let message: string = 'An error has occurred!';
	let timer: number = 5;
	if ($page.error != null) message = $page.error.message;
</script>

<div class="container h-full space-y-10 mx-auto max-w-xl flex flex-col justify-center items-center">
	<div class="flex flex-row">
		<h1>{message}</h1>
		<ProgressRadial />
	</div>

	<div>
		<h5>Redirecting you back home in {timer} seconds...</h5>
	</div>
</div>
