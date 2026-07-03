from transformers import BigBirdConfig as BigBirdConfig, BigBirdForPreTraining as BigBirdForPreTraining, BigBirdForQuestionAnswering as BigBirdForQuestionAnswering, load_tf_weights_in_big_bird as load_tf_weights_in_big_bird
from transformers.utils import logging as logging

def convert_tf_checkpoint_to_pytorch(tf_checkpoint_path, big_bird_config_file, pytorch_dump_path, is_trivia_qa) -> None: ...
