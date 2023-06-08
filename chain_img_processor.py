from jaa import JaaCore

from termcolor import colored, cprint

from typing import Any

version = "2.1.0"

class ChainImgProcessor(JaaCore):
    def __init__(self):
        JaaCore.__init__(self)

        self.processors:dict = {
        }

        self.default_chain = ""
        self.init_on_start = ""

        self.inited_processors = []

    def process_plugin_manifest(self, modname, manifest):
        # adding processors from plugin manifest
        if "img_processor" in manifest:  # process commands
            for cmd in manifest["img_processor"].keys():
                self.processors[cmd] = manifest["img_processor"][cmd]

        return manifest

    def init_with_plugins(self):
        self.init_plugins(["core"])
        #self.init_plugins()
        self.display_init_info()

        #self.init_translator_engine(self.default_translator)
        init_on_start_arr = self.init_on_start.split(",")
        for proc_id in init_on_start_arr:
            self.init_processor(proc_id)

    def run_chain(self, img, params:dict[str,Any] = None, chain:str = None):
        if chain is None:
            chain = self.default_chain
        if params is None:
            params = {}

        chain_ar = chain.split(",")
        # init all not inited processors first
        for proc_id in chain_ar:
            if proc_id != "":
                if not proc_id in self.inited_processors:
                    self.init_processor(proc_id)

        # run processing
        for proc_id in chain_ar:
            if proc_id != "":
                img = self.processors[proc_id][1](self, img, params) # params can be modified inside

        return img, params

    # ---------------- init translation stuff ----------------
    def init_processor(self, processor_id: str):
        if processor_id == "": # blank line case
            return

        if processor_id in self.inited_processors:
            # already inited
            return

        try:
            self.print_blue("TRY: init processor plugin '{0}'...".format(processor_id))
            self.processors[processor_id][0](self)
            self.inited_processors.append(processor_id)
            self.print_blue("SUCCESS: '{0}' inited!".format(processor_id))

        except Exception as e:
            self.print_error("Error init processor plugin {0}...".format(processor_id), e)

    # ------------ formatting stuff -------------------
    def display_init_info(self):
        cprint("ChainImgProcessor v{0}:".format(version), "blue", end=' ')
        self.format_print_key_list("processors:", self.processors.keys())

    def format_print_key_list(self, key:str, value:list):
        print(colored(key+": ", "blue")+", ".join(value))

    def print_error(self,err_txt,e:Exception = None):
        cprint(err_txt,"red")
        # if e != None:
        #     cprint(e,"red")
        import traceback
        traceback.print_exc()

    def print_red(self,txt):
        cprint(txt,"red")

    def print_blue(self, txt):
        cprint(txt, "blue")
