"""From skel file to json."""
import json
from pathlib import Path
from zipfile import ZipFile

TF_S3_ROOT = "https://templateflow.s3.amazonaws.com"
TF_GH_ROOT = "https://raw.githubusercontent.com/templateflow"


def get_parser():
    """Build parser object."""
    from argparse import ArgumentParser
    from argparse import RawTextHelpFormatter

    parser = ArgumentParser(description="""NiWorkflows Utilities""",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument('input_file', action='store', type=Path, help='the input file')
    parser.add_argument('output_file', action='store', type=Path,
                        help='the output directory')

    return parser


def _leafnode(entry):
    filename = entry[-1]
    node = {
        "text": filename,
        "icon": "fa fa-file",
    }
    if filename.rstrip(".gz").endswith(".nii"):
        node["icon"] = "fas fa-brain" if "_atlas-" not in filename else "fas fa-globe"
        if "_mask.nii" in filename:
            node["icon"] = "fas fa-crop-alt"
        node["href"] = "/".join([TF_S3_ROOT] + entry)
        return node

    if filename.rstrip(".gz").endswith(".gii"):
        node["icon"] = "fas fa-draw-polygon"
        node["href"] = "/".join([TF_S3_ROOT] + entry)
        return node

    if ("_from-" in filename or "_to-" in filename) and "_xfm" in filename:
        node["icon"] = "fas fa-route"
        node["href"] = "/".join([TF_S3_ROOT] + entry)
        return node

    if filename in ("LICENSE", "LICENCE", "COPYING"):
        node["icon"] = "fab fa-creative-commons-share"

    if filename.startswith("CHANGE"):
        node["icon"] = "fas fa-clipboard-list"

    if filename.rstrip(".gz").endswith(".tsv"):
        node["icon"] = "fas fa-table"

    if filename.endswith(".json"):
        node["icon"] = "fas fa-file-alt"

    if filename.endswith(".py"):
        node["icon"] = "fab fa-python"

    node["href"] = "/".join([TF_GH_ROOT] + [entry[0]] + ["master"] + entry[1:])

    return node


def main(args=None):
    """Entry point."""
    opts = get_parser().parse_args(args=args)

    with ZipFile(str(opts.input_file), 'r') as zfo:
        archive_index = zfo.namelist()
    archive_split = [[bit for bit in path.split('/') if bit] for path in sorted(archive_index)]
    root = {tpl[0]: {"text": tpl[0], "icon": "fa fa-folder", "nodes": []}
            for tpl in archive_split if len(tpl) == 1}
    for entry in archive_split:
        if len(entry) == 1:
            continue

        tpl = entry[0]
        leaf = entry[-1]
        if leaf.startswith('cohort-') or leaf == "scripts":
            root[tpl]["nodes"].append({
                "text": leaf,
                "icon": "fas fa-users" if leaf.startswith("cohort") else "fa fa-folder",
                "nodes": [],
            })
            continue

        leafnode = _leafnode(entry)
        if len(entry) == 3:
            cohort = entry[1]
            subnodenames = [n["text"] for n in root[tpl]["nodes"]]
            index = subnodenames.index(cohort)
            root[tpl]["nodes"][index]["nodes"].append(leafnode)
            continue

        if len(entry) > 3:
            print(entry)
            continue

        root[tpl]["nodes"].append(leafnode)

    opts.output_file.write_text(json.dumps(list(root.values()), indent=2))


if __name__ == '__main__':
    from sys import argv
    main(args=argv[1:])
