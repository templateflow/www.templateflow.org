
!!! info "Who is this tutorial for?"

	First, this is intended for those wishing to add templates to TemplateFlow. Second, this is for people who want to add a template directory that does not already exists. TemplateFlow consists of multiple templates sorted by the space the template is in. This tutorial tells you how to add a new template space.

	If you want to fix, improve or extend an existing template please refer to the _Updating templates_ documentation (work in progress).

	This tutorial assumes you have read and understood the [contributing guidelines](guidelines.md).

## Overview: Submission pipeline and the _TemplateFlow Manager_ tool

| ![Manager](../assets/templateflow_fig-manager.png) |
|:--:| 
| To contribute a new template to _TemplateFlow_, members of the community first organise template resources to conform to the BIDS-like _TemplateFlow_ structure. Next, the _TemplateFlow Manager_ tool (`tfmgr`) synchronises the resources to OSF cloud storage and opens a new pull request proposing the addition of the new template. A subsequent peer-review process ensures that all data are conformant with the _TemplateFlow_ standard. Finally, _TemplateFlow_ curators conclude the peer-review process with the merge of the pull request, thereby adding the template into the _TemplateFlow Archive_. |

## Step 1: Organize your template tree

TemplateFlow follows a BIDS-like structure, please make sure your tree is formatted following the [naming conventions](naming.md).

!!! info "Examples"

    Please check the formatting of existing templates in the [Archive browser](../browse.md)

## Step 2: Install the *TemplateFlow Manager*

Installing the manager is as easy as:

```Shell
pip install git+https://github.com/templateflow/python-manager@master
```

Once the manager is installed, you should be able to print out its version:

```Shell
$ tfmgr --version
TF Archive manager 20.0.0
```

## Step 3: Prepare your credentials for authentication

**On OSF.io**: First, generate a personal authentication token (PAT) to authenticate your username and be able to upload data to OSF.
Good guidelines [on how to create your PAT on OSF are given here](https://mjaquiery.github.io/jspsych-born-open-data/osf-pat/index.html).

**On GitHub**: Then, you also want to generate a PAT to authenticate against GitHub.
If you are unsure of how to properly create one, please follow the [official guidelines](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), in particular, it is likely easier to avoid permissions problems if you take the [classic tokens route](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).

!!! critical "Make sure you store both tokens safely and that you will be able to retrieve them later"

**At this point, you can set up your credentials**

```Shell
$ export OSF_TOKEN='<copy and paste your OSF PAT here>'
$ export GITHUB_USER='<your GitHub handle>'  # For instance, 'oesteban'
$ export GITHUB_TOKEN='<copy and paste your GitHub PAT here>'
```

## Step 4: Add your template with `tfmgr add`

```Shell
# Assuming the template is at the current directory, under tpl-Name/
$ tfmgr add tpl-Name'
```

## Finished: The peer-review process is now initiated

Once `tfmgr add` has concluded successfully, you'll be provided with a URL that points to a newly created PR against the templateflow superdataset.
That means your PR will now be listed at the [`templateflow/templateflow` repo](https://github.com/templateflow/templateflow/pulls).
Now, the [*TemplateFlow* maintainers](https://github.com/orgs/templateflow/teams/maintainers) will carry out *editorial management* of your proposed template and have it peer-reviewed before it is finally *merged* into *TemplateFlow*.

## Wrapping up

This screencast summarizes the three-step process above:

<script id="asciicast-331256" src="https://asciinema.org/a/331256.js" async data-autoplay="true" data-speed="4" data-theme="tango"></script>
