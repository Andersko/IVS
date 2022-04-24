#
# Makefile
#

TARGET       = calculator.py
PROFILE      = profile.py
PROFILE_DATA = data.txt

PYTHON  = python3
DOXYGEN = doxygen
RM      = rm -rf
ZIP     = zip

DOC_DIR     = ../../doc
INSTALL_DIR = ../../install
REPO_DIR    = ../../repo
IVS_DIR     = ..

PACK_WIS       = pack-wis.zip
PACK_WIS_FILES = hodnoceni.txt dokumentace.pdf odevzdani.txt src/

PACK_IVS       = xpavlo14
PACK_IVS_FILES = $(DOC_DIR) $(INSTALL_DIR) $(REPO_DIR)

.PHONY: all pack pack-wis pack-ivs repo clean test doc run profile installer

all: doc

pack: doc installer pack-wis pack-ivs

pack-wis: $(PACK_WIS_FILES)
	$(ZIP) $(PACK_WIS) $(PACK_WIS_FILES)
	@echo "Rename archive $(PACK_WIS) and submit archive in wis";

pack-ivs: repo
	$(ZIPT) $(PACK_IVS) $(PACK_IVS_FILES)

repo:
	cp -r $(IVS_DIR) $(REPO_DIR)

clean:
	$(RM) $(DOC_DIR) $(INSTALL_DIR) $(REPO_DIR)

test:
	$(PYTHON) -m unittest

doc:
	mkdir -p $(DOC_DIR)
	$(DOXYGEN)

run:
	./$(TARGET)

profile:
	./$(PROFILE) < $(PROFILE_DATA)
