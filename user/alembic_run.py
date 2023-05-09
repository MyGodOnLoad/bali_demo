from alembic import command
from alembic.config import Config

if __name__ == '__main__':
    alembic_cfg = Config('alembic.ini')
    alembic_cfg.set_main_option('script_location', 'alembic')
    command.revision(alembic_cfg, autogenerate=True, message='create users table')

