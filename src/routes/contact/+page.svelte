<script lang="ts">
	import BlogHeader from '$lib/BlogHeader.svelte';
	import { clipboard } from '@skeletonlabs/skeleton';
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';

	function copyToClipboard() {
		const t: ToastSettings = {
			message: 'Copied Discord ID to clipboard!'
		};
		toastStore.trigger(t);
	}
</script>

<Toast />

<div class="container h-full mx-auto flex flex-col justify-center text-center">
	<div class="space-y-5">
		<BlogHeader title={'Contact Me'} date="" />

		<h4>Some of my contact information</h4>

		<ul>
			<li>GitHub: <a href="https://github.com/jjoeldaniel">jjoeldaniel</a></li>
			<li>
				Discord:
				<button
					class="text-blue-500 hover:text-blue-700"
					on:click={copyToClipboard}
					use:clipboard={'joel#0005'}
				>
					joel#0005
				</button>
			</li>
			<li>Twitter: <a href="https://twitter.com/jjoeldaniel">jjoeldaniel</a></li>
		</ul>
	</div>
</div>
