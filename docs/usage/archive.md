
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
          url : "../../assets/templateflow.json",
          dataType: "text",
          success : function (tree) {
              $('#tree').bstreeview({ data: tree });
          }
      });
});
</script>


[3]: https://datalad.org "DataLad"
[4]: https://github.com/templateflow/templateflow "TemplateFlow repository"
