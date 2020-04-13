
The _TemplateFlow Archive_ aggregates all the templates for redistribution.
The archive uses [DataLad][3] to maintain all templates under version control.

## Accessing the Archive via the Python client

The recommended way to use TemplateFlow is via the [Python Client](client.md)

## Accessing the Archive via DataLad

First, make sure you have a functional installation of DataLad.
The archive has a top-level data structure to maintain all templates.
This is the _super-dataset_, and it is maintained on [GitHub][4].
The latest stable super-dataset can be referenced with `///templateflow`:

``` bash
$ datalad install -r ///templateflow
```

The `-r` switch ensures all available templates are also _installed_.

Once the super-dataset and its siblings are installed, metadata will be already accessible.
However, the different imaging data resources (NIfTI, GIFTI and transforms files) have to be pulled down.

For example, to download the complete `tpl-MNI152NLin2009cAsym`:

``` bash
$ cd templateflow
$ datalad get -r tpl-MNI152NLin2009cAsym
```

## TemplateFlow's data structure

### Browse the archive

<div id="tree"></div>
<script>
    $(document).ready(function() {
      $.ajax({
          url : "../assets/templateflow.json",
          dataType: "text",
          success : function (tree) {
              $('#tree').bstreeview({ data: tree });
          }
      });
});
</script>


### Naming conventions

The TemplateFlow Archive is organized in a [BIDS-like structure](https://bids-specification.readthedocs.io/en/derivatives/).
However, it deviates from the standard at times (e.g., the `tpl` key replaces `sub`).
Here we outline the most common names that are found in TemplateFlow.

Common key names using in TemplateFlow:

Key | Entity | Description
--- | :-: | ---
`tpl` | Template identifier | A unique name of the template, matching those of BIDS.
`res` | Resolution | See `template_description.json` within each template for more information about what the index specifies.
`atlas` | Atlas | Name of an atlas.
`desc` | Description | Additional information about the file to differentiate it from other files.

TemplateFlow uses all the valid suffices of BIDS, but the most commonly found in the Archive are:

Suffix | Description
--- | ---
`dseg` | discrete segmentation
`pseg` | probability segmentation
`mask` | binary mask
`xfm` | transform file
`T2w` | T2 weighted image
`T1w` | T1 weighted image

Common file-formats used in TemplateFlow:

Extension | Description
--- | ---
`.nii.gz` | Image
`.tsv`    | Tabular information
`.json`   | Meta-information
`.h5`     | Transform file


Thus a template with the following name:
`tpl-test_res-high_atlas-myatlas_desc-200nodes_dseg.nii.gz` would be a
NIfTI image containing the discrete segmentation of `myatlas` that
contains `200nodes`. The template identifier is `test`.
The resolution information will be found in the `template_description.json`
file under the entry `high`.


[3]: https://datalad.org "DataLad"
[4]: https://github.com/templateflow/templateflow "TemplateFlow repository"