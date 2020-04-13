

Welcome to the *TemplateFlow* project!
We're excited you're here and want to contribute.

!!! info "Imposter's syndrome disclaimer"
    **Imposter's syndrome disclaimer**[^1]: We want your help. No, really.

    There may be a little voice inside your head that is telling you that
    you're not ready to be an open-source contributor; that your skills
    aren't nearly good enough to contribute. What could you possibly offer a
    project like this one?

    We assure you - the little voice in your head is wrong. If you can
    write code at all, you can contribute code to open-source. Contributing
    to open-source projects is a fantastic way to advance one's coding
    skills. Writing perfect code isn't the measure of a good developer (that
    would disqualify all of us!); it's trying to create something, making
    mistakes, and learning from those mistakes. That's how we all improve,
    and we are happy to help others learn.

    Being an open-source contributor doesn't just mean writing code, either.
    You can help out by writing documentation, tests, or even giving
    feedback about the project (and yes - that includes giving feedback
    about the contribution process). Some of these contributions may be the
    most valuable to the project as a whole, because you're coming to the
    project with fresh eyes, so you can see the errors and assumptions that
    seasoned contributors have glossed over.

## Joining the conversation

*TemplateFlow* is maintained by a growing group of enthusiastic developers&mdash;
and we're excited to have you join!
Most of our discussions will take place on open [issues][link_issues].

We also encourage users to report any difficulties they encounter on [NeuroStars][link_neurostars],
a community platform for discussing neuroimaging.

We actively monitor both spaces and look forward to hearing from you in either venue!

## Before you start

### Are you allowed to share the template?
Templates have a license to specify the terms under which they can be shared.
TemplateFlow can only include templates that allow for redistribution.
It is okay if the template requires attribution, but you need to make sure to
add the attribution information into the `template_description.json` file.

### What type of contribution are you making?
There are three different types of contributions you can make to TemplateFlow.

**A new template space**
:   This contribution involves adding a new space that does not
    currently exist. Let us say you have made a new pediatric space that
    you transform your images to; this would be a new template space.
    All the different MNI templates are each considered their own
    template space. Currently this requires writing permissions to the
    TemplateFlow repo. For now, if you do not have access open up an
    issue in the templateflow repo to say which template spaces should
    be added.

**NIfTI images within an existing template space**
:   This contribution involves adding to a template space that currently
    exists. An example of this would be adding a NIfTI file that is an
    atlas. You need to know which template space your atlas is in (Note:
    there are multiple MNI spaces).

**Meta information**
:   This contribution involves additional information about existing
    templates. These will generally be in `.json` or `.tsv` files. There
    are also transform files which help translate between templates.

**Python client**
:   You are implementing a new feature or fixing a bug of the Python client.
    Or you are improving its documentation. Please refer to the
    [Python client](client.md) area.

There are tutorials for each of these different types of contributions.

## Template Style Guide

Please check [the documentation](archive.md) about how templates are structure
and appropriate names for their files.

## Recognizing contributions

We welcome and recognize all contributions regardless their size, content or scope:
from documentation to testing and code development.

## Thank you!

You're awesome. :wave::smiley:

<br>

*&mdash; Based on contributing guidelines from the [STEMMRoleModels][link_stemmrolemodels] project.*

[^1]: The imposter syndrome disclaimer was originally written by
    [Adrienne Lowe](https://github.com/adriennefriend) for a
    [PyCon talk](https://www.youtube.com/watch?v=6Uj746j9Heo), and was
    adapted based on its use in the README file for the
    [MetPy project](https://github.com/Unidata/MetPy).

[link_stemmrolemodels]: https://github.com/KirstieJane/STEMMRoleModels
[link_neurostars]: https://neurostars.org/tags/fmriprep
[link_issues]: https://github.com/templateflow/templateflow/issues
