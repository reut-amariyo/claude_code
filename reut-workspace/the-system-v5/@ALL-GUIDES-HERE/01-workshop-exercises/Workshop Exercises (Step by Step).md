### Preparation: Installing the Project Files

1. Download the ZIP file and extract it.
2. Drag the extracted folder into your Obsidian Vault.
3. On Windows? It sometimes creates an extra ".obsidian" folder inside the Vault. Ignore it.
4. Make sure you can see all folders (A-agents, B-brain, C-core, T-tools, etc.) in the left sidebar in Obsidian. They're inside the the-system folder you extracted from the ZIP file.

### Preparation: Opening Claude Code

4. Open a new session in Claude Code.
5. **Important:** Select the the-system folder as your working directory. This is how Claude knows where to read, edit, and create files.

---

### Step 1: Choose Your Track

Before you start, pick the track that fits your work:

**Content** Social media posts, content creation, personal brand.
**Research** Executive briefings, competitor analysis, market research.
**Communication** Professional emails, client messages, outreach.

**Working with your own business?** Open `T-tools/02-prompts/` and go into your track folder (content, research, or communication).

From now on, all your prompts (01 through 04) are inside that one folder. Just follow them in order.

---

### Step 2: Fill in Your Business Information

Open the file `B-brain/brand-discovery-worksheet.md`

Fill in the text with your information (copy-paste from the document you filled in beforehand).

**Do not change file names.** The prompts are linked to them.

---

### Step 3: Prepare Writing Samples

Open the samples folder that matches your track:
- **Content** → `B-brain/content-samples/`
- **Communication** → `B-brain/communication-samples/`
- **Research** → `B-brain/research-samples/`

Paste your text (Hebrew or English) into each of the 3 files: `sample-01`, `sample-02`, `sample-03`.

### Step 4: Run the 4 Prompts

**Run one prompt at a time. Wait for it to finish before pasting the next one.**

All 4 prompts are inside your track folder. Just go in order:

**Prompt 1. Convert Brand Discovery**

- Copy the entire content of `01-convert-brand-discovery.md`
- Paste it in Claude Code and send.
- Claude reads the Brand Discovery and automatically updates the C-core files: `project-brief`, `icp-profile`, `voice-dna`.

**Prompt 2. Learn My Writing Style**

- Copy `02-learn-my-writing-style.md` and paste it.
- Claude reads the 3 samples and updates the Core documents, the agents, and Memory.

**Prompt 3. Sync the Agents**

- Copy `03-sync-agents-with-context.md` and paste it.
- Claude makes sure all agents know and understand the full context that was defined.

**Prompt 4. Create Your Output**

- Copy the `04-...` file from your track folder and paste it.
- Fill in the details (your topic, idea, or recipient depending on the track).
- Claude uses the agents, skills, and all your settings to create the output.

What each track produces:

- **Content** A social media post ready to publish (LinkedIn, Facebook, Instagram, Twitter/X)
- **Research** A structured executive briefing ready to use
- **Communication** A professional email ready to send

---

### Important Tip: Permissions

When Claude asks for permission to read or edit files, click **"Allow always for session"** so you don't have to approve each action separately.

---

### What Happens Next?

- Your output is saved in the `O-output/` folder as a new file. You can read it both in Obsidian and in Claude's chat.
- Want to keep going? There are bonus prompts (5-14) in `T-tools/02-prompts/BONUS/` for creating new agents, skills, API connections, The Loop, and more.
- You can also try a different track. Pick a different track folder and run Prompt 4 again to see the same system produce a completely different output.

Yalla, good luck.
