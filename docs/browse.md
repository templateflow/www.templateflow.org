# The _TemplateFlow Archive_ online browser

Template data are archived using a BIDS-like directory structure, with top-level directories for each template.
Each directory contains image files, annotations, and metadata for that template. Following BIDS specifications, volumetric data are stored in NIfTI format and surface data with the GIFTI2 format.

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