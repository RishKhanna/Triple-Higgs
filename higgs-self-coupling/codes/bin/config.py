# Constants
HOME_DIR = '/home2/ashu_bharadwaj/higgs-self-coupling/'
CODE_DIR = HOME_DIR + 'codes/bin/'
DELPHES_FILE = '/Events/run_01/tag_1_delphes_events.root'
MADGRAPH_DIR = '/home2/ashu_bharadwaj/apps/madgraph/'
DATASET_DIR = HOME_DIR + 'datasets/csvdata/'
TXT_DIR = '/home2/ashu_bharadwaj/scratch/'
OUTPUT_DIR = '/scratch/higgs-self-coupling-decay/'
GIT_DIR = '/home2/ashu_bharadwaj/higgs-self-coupling/'
MN2 = 750

RUN_MADGRAPH = True
RUN_PYTHIA = True
RUN_DELPHES = True
RUN_ANALYSIS = True

# Specific Parameters
EVENT_NAME = 'hh'
SIGNAL = True

# Hyper Parameters
NUM_RUNS = 1               # Number of EVENTS_NUM event runs
EVENT_NUM = int(1e2)        # Number of events to generate per run
START_SEED = 25              # The starting seed
