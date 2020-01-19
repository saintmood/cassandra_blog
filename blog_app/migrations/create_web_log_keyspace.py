from cassandra.cluster import Cluster


cluster = Cluster()
session = cluster.connect(wait_for_all_pools=True)
session.execute(
    """
    CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION={'class': 'SimpleStrategy', 'replication_factor': %s};
    """ % 
    ("weblog", 2,)
)