# AIVoiceprint
项目名称：声纹识别
主要功能：通过声音识别人物
实现原理（流程）：
  音频 → 提取语音特征（FFT、Mel过滤、MFCC）→ CNN&GRU → Triplet loss损失函数训练 + 预训练  + 训练得结果
