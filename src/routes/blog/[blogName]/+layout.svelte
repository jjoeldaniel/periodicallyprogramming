<script lang="ts">
	// The ordering of these imports is critical to your app working properly
	import '@skeletonlabs/skeleton/themes/theme-crimson.css';
	import '@skeletonlabs/skeleton/styles/all.css';
	// Most of your app wide CSS should be put in this file
	import '../../../app.postcss';
	import { TableOfContents } from '@skeletonlabs/skeleton';
	import { AppShell } from '@skeletonlabs/skeleton';
</script>

<AppShell>
	<svelte:fragment slot="sidebarRight">
		<div class="2xl:flex hidden py-20 px-3 fixed top-0 right-0">
			<TableOfContents target="#page" />
		</div>
	</svelte:fragment>
	<slot />
</AppShell>
