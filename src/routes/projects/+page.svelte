<script>
	import { Avatar } from '@skeletonlabs/skeleton';
	import avatar from '$lib/images/avatar.png';
	import password from '$lib/images/password.png';
	import data_science from '$lib/images/data_science.png';
	import glass from '$lib/images/glass.jpg';
</script>

<div
	class="container h-full space-y-10 -translate-y-[-2%] 2xl:-translate-y-[-7%] mx-auto flex max-w-xl flex-col justify-center items-center"
>
	<div class="space-y-4">
		<h1 class="text-center"><strong>Projects</strong></h1>
		<h1 class="text-center"><strong>🚧</strong></h1>
		<p>Here are some of my personal projects!</p>
	</div>

	<div class="flex flex-col columns-2 space-y-10 pb-20">
		<div class="card card-hover overflow-hidden">
			<header>
				<a href="https://github.com/jjoeldaniel/jpass">
					<img src={password} class="bg-black/50 w-full aspect-[21/9]" alt="Post" />
				</a>
			</header>
			<div class="p-4 space-y-4">
				<h6 class="h6" data-toc-ignore>Python, Flask, Postgres, JavaScript</h6>
				<h3 class="h3">JPass</h3>
				<article>
					<p>
						A password manager for securely storing user passwords with bcrypt, a password-hashing
						function
					</p>
					<br />
					<ol class="list">
						<li>
							<span>1.</span>
							<span class="flex-auto">
								Implemented login and signup flow with OpenID and OAuth support for Google and Email
								authentication
							</span>
						</li>
						<li>
							<span>2.</span>
							<span class="flex-auto">Created accessible, mobile-friendly web user interface</span>
						</li>
						<li>
							<span>3.</span>
							<span class="flex-auto">
								Built with Python and Flask framework, with a relational database for storing
								encrypted user passwords
							</span>
						</li>
					</ol>
				</article>
			</div>
			<hr class="opacity-50" />
			<footer class="p-4 flex justify-start items-center space-x-4">
				<Avatar class="mx-auto" src={avatar} width="w-8" rounded="rounded-full" />
				<div class="flex-auto flex justify-between items-center">
					<h6 class="font-bold">By Joel</h6>
					<small>March 2023</small>
				</div>
			</footer>
		</div>
		<div class="card card-hover overflow-hidden">
			<header>
				<a href="https://github.com/jjoeldaniel/jpass">
					<img src={data_science} class="bg-black/50 w-full aspect-[21/9]" alt="Post" />
				</a>
			</header>
			<div class="p-4 space-y-4">
				<h6 class="h6" data-toc-ignore>Rust</h6>
				<h3 class="h3">keyphrases.rs</h3>
				<article>
					<p>
						An open-source library for efficient and accurate extraction of keywords from large
						volumes of text
					</p>
					<br />
					<ol class="list">
						<li>
							<span>1.</span>
							<span class="flex-auto">
								Implemented Rapid Automatic Keyword Extraction (RAKE) algorithm
							</span>
						</li>
						<li>
							<span>2.</span>
							<span class="flex-auto"
								>Designed the library to be flexible, customizable, and scalable, allowing users to
								adjust the library’s parameters and configurations to fit their needs</span
							>
						</li>
						<li>
							<span>3.</span>
							<span class="flex-auto">
								Optimized the library’s performance and memory usage to ensure efficient processing
								of large volumes of text data
							</span>
						</li>
						<li>
							<span>4.</span>
							<span class="flex-auto">
								Contributed to the open-source community by sharing the library’s source code and
								documentation on GitHub and crates.io
							</span>
						</li>
					</ol>
				</article>
			</div>
			<hr class="opacity-50" />
			<footer class="p-4 flex justify-start items-center space-x-4">
				<Avatar class="mx-auto" src={avatar} width="w-8" rounded="rounded-full" />
				<div class="flex-auto flex justify-between items-center">
					<h6 class="font-bold">By Joel</h6>
					<small>March - May 2023</small>
				</div>
			</footer>
		</div>
		<div class="card card-hover overflow-hidden">
			<header>
				<a href="https://github.com/jjoeldaniel/jpass">
					<img src={glass} class="bg-black/50 w-full aspect-[21/9]" alt="Post" />
				</a>
			</header>
			<div class="p-4 space-y-4">
				<h6 class="h6" data-toc-ignore>Python, KeyBERT</h6>
				<h3 class="h3">Trends Analysis</h3>
				<article>
					<p>
						Identifies key trends and patterns in user activity, including peak hours of usage, most
						popular channels, and frequently used words and phrases.
					</p>
					<br />
					<ol class="list">
						<li>
							<span>1.</span>
							<span class="flex-auto">
								Conducted data analysis on a Discord server with over 1,000 members to identify
								trends and patterns in user behavior
							</span>
						</li>
						<li>
							<span>2.</span>
							<span class="flex-auto">
								Utilized a Bidirectional Encoder Representations from Transformers (BERT) model
								library to extract relevant keywords from Discord messages</span
							>
						</li>
						<li>
							<span>3.</span>
							<span class="flex-auto">
								Extracted relevant data using Discord API and web scraping techniques to collect
								information on user activity, message content, and channel usage
							</span>
						</li>
						<li>
							<span>4.</span>
							<span class="flex-auto">
								Visualized data using charts, graphs, and other visualization tools to highlight
								trends and patterns in user behavior
							</span>
						</li>
					</ol>
				</article>
			</div>
			<hr class="opacity-50" />
			<footer class="p-4 flex justify-start items-center space-x-4">
				<Avatar class="mx-auto" src={avatar} width="w-8" rounded="rounded-full" />
				<div class="flex-auto flex justify-between items-center">
					<h6 class="font-bold">By Joel</h6>
					<small>January - May 2023</small>
				</div>
			</footer>
		</div>
	</div>
</div>
