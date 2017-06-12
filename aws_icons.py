"""
Annotate Terraform graphs with AWS icons.

Usage: Takes graphviz input from `terraform graph` on stdin and ouputs graphviz
to stdout.
"""
import os
import re
import sys


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

ICONS = {
    'aws_autoscaling_group': 'Compute_AmazonEC2_AutoScaling.png',
    'aws_db_instance': 'Database_AmazonRDS_RDSDBinstance.png',
    'aws_db_subnet_group': '',
    'aws_ebs_volume': 'Storage-Content-Delivery_AmazonEBS.png',
    'aws_elasticache_cluster': 'Database_AmazonElasticCache.png',
    'aws_elasticache_subnet_group': '',
    'aws_elb': 'Compute_ElasticLoadBalancing.png',
    'aws_iam_access_key': 'Security-Identity_AWSIAM_addon.png',
    'aws_iam_instance_profile': 'Security-Identity_AWSIAM.png',
    'aws_iam_role_policy': '',
    'aws_iam_user': 'General_user.png',
    'aws_iam_user_policy': '',
    'aws_launch_configuration': '',
    'aws_iam_role': 'Security-Identity_AWSIAM_role.png',
    'aws_instance': 'Compute_AmazonEC2_instance.png',
    'aws_route53_record': 'Networking_AmazonRoute53.png',
    'aws_s3_bucket': 'Storage-Content-Delivery_AmazonS3_bucket.png',
    'aws_security_group': '',
    'aws_volume_attachment': '',
    'aws_eip': 'Compute_AmazonEC2_ElasticIP.png',
    'aws_ecs_cluster': 'Compute_AmazonECS.png',
    'aws_ami': 'Compute_AmazonEC2_AMI.png',
    'aws_vpc': 'General_virtualprivatecloud.png',
    'aws_internet_gateway': 'Networking_AmazonVPC_internetgateway.png',
    'aws_nat_gateway': 'Networking_AmazonVPC_VPCNATgateway.png',
    'aws_route_table': 'Networking_AmazonRoute53_routetable.png',
    'aws_route53_zone': 'Networking_AmazonRoute53_hostedzone.png',
    'aws_key_pair': 'SecurityIdentityCompliance_IAM_long-termsecuritycredential.png',
    'aws_s3_bucket_object': 'Storage-Content-Delivery_AmazonS3_object.png',
    'aws_subnet': 'Compute_AmazonVPC_router.png',
    'aws_iam_server_certificate': 'SecurityIdentityCompliance_AWSCertificateManager_certificatemanager.png',
    'aws_ecs_task_definition': 'ManagementTools_AWSCloudFormation_template.png',
    'aws_ecs_service': 'Compute_AmazonECS_EC2ComputeContainer.png',
}


def repl_func(matchobj):
    resource_type = matchobj.group(2)
    icon = ICONS.get(resource_type)
    if icon is None:
        sys.stderr.write('Unknown resource: {}\n'.format(resource_type))
    if not icon:
        return matchobj.group(0)

    return (
        'label = <<TABLE BORDER="0"><TR><TD><IMG SRC="{1}"/></TD><TD>{0}</TD></TR></TABLE>>,'
        .format(
            matchobj.group(1),
            os.path.join(BASE_DIR, 'icons', icon),
        )
    )


def main():
    text = sys.stdin.read()

    new_text = re.sub(r'label = "(?:module\..*?\.){0,1}((aws_.+)\..+)",', repl_func, text)

    sys.stdout.write(new_text)


if __name__ == '__main__':
    main()
