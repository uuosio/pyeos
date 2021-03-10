import _chainapi
import json

class ChainApi(object):

    def __init__(self, chain):
        self.ptr = chain.ptr
        self.chain = chain

    def get_info(self):
        return _chainapi.get_info(self.ptr)

    def get_activated_protocol_features(self, params: dict):
        return _chainapi.get_activated_protocol_features(self.ptr, params)

    def get_block(self, params: dict):
        return _chainapi.get_block(self.ptr, params)

    def get_block_header_state(self, params: dict):
        return _chainapi.get_block_header_state(self.ptr, params)

    def get_account(self, account: str):
        args = {'account_name': account}
        args = json.dumps(args)
        ret, result = _chainapi.get_account(self.ptr, args)
        if not ret:
            raise Exception(result)
        result = json.loads(result)
        return ret, result

    def get_code(self, params: dict):
        return _chainapi.get_code(self.ptr, params)

    def get_code_hash(self, params: dict):
        return _chainapi.get_code_hash(self.ptr, params)

    def get_abi(self, account):
        params = dict(account_name=account)
        params = json.dumps(params)
        success, result = _chainapi.get_abi(self.ptr, params)
        if not success:
            raise Exception(result)
        return json.loads(result)

    def get_raw_code_and_abi(self, params: dict):
        return _chainapi.get_raw_code_and_abi(self.ptr, params)

    def get_raw_abi(self, params: dict):
        return _chainapi.get_raw_abi(self.ptr, params)

    def get_table_rows(self, params: dict):
        params = json.dumps(params)
        success, ret = _chainapi.get_table_rows(self.ptr, params)
        print(success, ret)
        if not success:
            raise Exception(ret)
        return json.loads(ret)

    def get_table_by_scope(self, params: dict):
        return _chainapi.get_table_by_scope(self.ptr, params)

    def get_currency_balance(self, params: dict):
    # struct get_currency_balance_params {
    #   name             code;
    #   name             account;
    #   optional<string> symbol;
    # };
        return _chainapi.get_currency_balance(self.ptr, params)

    def get_currency_stats(self, params: dict):
        return _chainapi.get_currency_stats(self.ptr, params)

    def get_producers(self, params: dict):
        return _chainapi.get_producers(self.ptr, params)

    def get_producer_schedule(self, params: dict):
        return _chainapi.get_producer_schedule(self.ptr, params)

    def get_scheduled_transactions(self, params: dict):
        return _chainapi.get_scheduled_transactions(self.ptr, params)

    def abi_json_to_bin(self, params: dict):
        return _chainapi.abi_json_to_bin(self.ptr, params)

    def abi_bin_to_json(self, params: dict):
        return _chainapi.abi_bin_to_json(self.ptr, params)

    def get_required_keys(self, params: dict):
        return _chainapi.get_required_keys(self.ptr, params)

    def get_transaction_id(self, params: dict):
        return _chainapi.get_transaction_id(self.ptr, params)

    def recover_reversible_blocks(self, old_reversible_blocks_dir: str, new_reversible_blocks_dir: str, reversible_cache_size: int=340*1024*1024, truncate_at_block: int=0):
        return _chainapi.recover_reversible_blocks(old_reversible_blocks_dir, new_reversible_blocks_dir, reversible_cache_size, truncate_at_block)

    def repair_log(self, blocks_dir: str, truncate_at_block: int=0):
        return _chainapi.repair_log(blocks_dir, truncate_at_block)

    def db_size_api_get(self):
        return _chainapi.db_size_api_get(self.ptr)

def repair_log(blocks_dir, truncate_at_block: int=0):
    return _chainapi.repair_log(blocks_dir, truncate_at_block)

def recover_reversible_blocks(old_reversible_blocks_dir: str, new_reversible_blocks_dir: str, reversible_cache_size: int=340*1024*1024, truncate_at_block: int=0):
    return _chainapi.recover_reversible_blocks(old_reversible_blocks_dir, new_reversible_blocks_dir, reversible_cache_size, truncate_at_block)
