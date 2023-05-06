<script lang="ts">
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
