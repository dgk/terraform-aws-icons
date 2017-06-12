Terraform AWS Icons
===================

Combine `Terraform graph`_ and `AWS Icons`_.

.. _Terraform graph: https://www.terraform.io/docs/commands/graph.html
.. _AWS Icons: https://aws.amazon.com/architecture/icons/


Usage
-----
Install the original from `pip`
::

    pip install terraform-aws-icons
    terraform graph | terraform-iconify | dot -Tpng > graph.png

or install this fork from github
::

    git clone [repo]
    cd [repo]
    make test

Examples
--------

Based on output from https://github.com/hashicorp/terraform/tree/master/examples:

``aws-asg.dot``:

.. image:: examples/aws-asg.png

``aws-rds.dot``:

.. image:: examples/aws-rds.png


License
-------

AWS icons are included with permission from Amazon Web Services.
