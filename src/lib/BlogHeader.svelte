<script lang='ts'>
    import { Avatar } from '@skeletonlabs/skeleton';
    export let title: string = "Title";
    export let date: string = "Date";
</script>

<a href="https://github.com/jjoeldaniel">
    <Avatar class="mx-auto" src="https://avatars.githubusercontent.com/u/100006388?v=4" width="w-32" rounded="rounded-full" />
</a>
<h1 class="text-center">{title}</h1>
<p class="text-center">{date}</p>