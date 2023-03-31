"""add section_id column

Revision ID: 7bf4eac76958
Revises: 0d267ae11945
Create Date: 2023-02-27 00:17:13.935016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7bf4eac76958"
down_revision = "0d267ae11945"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("cre_links", schema=None) as batch_op:
        batch_op.drop_constraint("uq_cre_link_pair", type_="unique")
        batch_op.create_unique_constraint("uq_pair", ["group", "cre"])

    with op.batch_alter_table("cre_node_links", schema=None) as batch_op:
        batch_op.drop_constraint("uq_cre_node_link_pair", type_="unique")
        batch_op.create_unique_constraint("uq_pair", ["cre", "node"])

    with op.batch_alter_table("node", schema=None) as batch_op:
        batch_op.add_column(sa.Column("section_id", sa.String(), nullable=True))
        batch_op.drop_constraint("uq_node", type_="unique")
        batch_op.create_unique_constraint(
            "uq_node",
            [
                "name",
                "section",
                "subsection",
                "ntype",
                "description",
                "version",
                "section_id",
            ],
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("node", schema=None) as batch_op:
        batch_op.drop_constraint("uq_node", type_="unique")
        batch_op.create_unique_constraint(
            "uq_node",
            ["name", "section", "subsection", "ntype", "description", "version"],
        )
        batch_op.drop_column("section_id")

    with op.batch_alter_table("cre_node_links", schema=None) as batch_op:
        batch_op.drop_constraint("uq_pair", type_="unique")
        batch_op.create_unique_constraint("uq_cre_node_link_pair", ["cre", "node"])

    with op.batch_alter_table("cre_links", schema=None) as batch_op:
        batch_op.drop_constraint("uq_pair", type_="unique")
        batch_op.create_unique_constraint("uq_cre_link_pair", ["group", "cre"])

    # ### end Alembic commands ###