import os
import requests
import pydicom
import cv2

from .DCM_to_JPG import *



def download(uri, dcm_path, dcm_name, jpg_dir, jpg_name):
    # Ensure the download and save paths exist
    os.makedirs(dcm_path, exist_ok=True)
    os.makedirs(jpg_dir, exist_ok=True)

    # Full paths for the saved files
    dicom_file_path = os.path.join(dcm_path, dcm_name)
    jpg_file_path = os.path.join(jpg_dir, jpg_name)
    
    # Download the DICOM file with streaming
    response = requests.get(uri, stream=True)
    response.raise_for_status()  # Raise an error for bad status

    # Save the DICOM file in chunks
    with open(dicom_file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):  # Adjust chunk_size if needed
            file.write(chunk)
    
    
    # Convert the DICOM file to JPG
    convert_dicom_to_jpg(dicom_file_path, jpg_dir, jpg_name)

# Example usage
if __name__ == "__main__":
    uri = "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/54ab613d-54d8-43d9-9415-f68cb73c85ea?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=142e34ccc02b2c34343c4d42851361214ca999611040b2d015e0bdeb86ee7b11b66199af6bb0c10623c86f1e94ff4765354be7ca7188fd1d7dcf7f2a5be42dae4b7b9eb4df818d65fbe2cd4e4a321e930fd5689d4b468b417cf9b9492986b96add0c59baf4d040be7929542dfff765cf3263cb2688bb067b10bcee7ce7764d029d1c28d124be229a4f93d37c82b5ef54c48f73736f6fc0d4cc9fbfbee976ae7d50b3589ef2828f7aebf13a17d3a017ef6db0d6152013c75a86f6c97217d0d07be2f6b033eb3dc922d4ff6acedf7daff63f7f480004eb12d2c69a41d030199fe6519d23cb963d5cb4e7de2e4ec7f7baac822bef184a4665eb573cd073626c4760"
    DCM_path = "D:/PROJECT/encord_T1/dataset/DCM files"
    DCM_name = "tet.dcm"
    JPG_dir = "D:/PROJECT/encord_T1/dataset/JPG files"
    JPG_name = "tet.jpg"

    download(uri, DCM_path, DCM_name, JPG_dir, JPG_name)
    


####### Code for parellel downloading (under development)
# import os
# import requests
# import concurrent.futures
# from DCM_to_JPG import *

# def download(uri, dcm_path, dcm_name, jpg_dir, jpg_name):
#     os.makedirs(dcm_path, exist_ok=True)
#     os.makedirs(jpg_dir, exist_ok=True)

#     dicom_file_path = os.path.join(dcm_path, dcm_name)
#     jpg_file_path = os.path.join(jpg_dir, jpg_name)
    
#     response = requests.get(uri, stream=True)
#     response.raise_for_status()

#     with open(dicom_file_path, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)
#     print(f"DICOM file downloaded and saved as {dicom_file_path}")
    
#     convert_dicom_to_jpg(dicom_file_path, jpg_dir, jpg_name)

# def download_and_convert_dicom_parallel(urls,name ,dcm_path, jpg_dir):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         futures = []
#         for i, uri in enumerate(urls):
#             dcm_name = f"{name}_{i}.dcm"
#             jpg_name = f"{name}_{i}.jpg"
#             futures.append(executor.submit(download, uri, dcm_path, dcm_name, jpg_dir, jpg_name))
#         concurrent.futures.wait(futures)

# # Example usage
# if __name__ == "__main__":
#     urls = ['https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/54ab613d-54d8-43d9-9415-f68cb73c85ea?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=142e34ccc02b2c34343c4d42851361214ca999611040b2d015e0bdeb86ee7b11b66199af6bb0c10623c86f1e94ff4765354be7ca7188fd1d7dcf7f2a5be42dae4b7b9eb4df818d65fbe2cd4e4a321e930fd5689d4b468b417cf9b9492986b96add0c59baf4d040be7929542dfff765cf3263cb2688bb067b10bcee7ce7764d029d1c28d124be229a4f93d37c82b5ef54c48f73736f6fc0d4cc9fbfbee976ae7d50b3589ef2828f7aebf13a17d3a017ef6db0d6152013c75a86f6c97217d0d07be2f6b033eb3dc922d4ff6acedf7daff63f7f480004eb12d2c69a41d030199fe6519d23cb963d5cb4e7de2e4ec7f7baac822bef184a4665eb573cd073626c4760', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/65fc04ee-1663-4b4c-be48-aae158c5fcaa?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=3e01d042dab1603aef370cf6fae4c0a44aabeb603e067c20ade03dfbfd7ab75c97cae1b54300d8ab161871d9c8768f851d4c66c74bfc56ee0a1daf6d1434530731e19a6a5f4e8a83c270556cc83f873c6928212d89069e8e4e68c6108e16c2327d5e1e3cf6dbba84789d54ec3a9c2883cc80eb50e16dee954ae3e07a8f76e7714cf8893560050c0930f81a855a495984889d9194cc15d3863b31e1241e0301071da7aca753d0924972d057738fec3822b83e715f77028c121b1914006be82487e8f6a49826cd8ea7fb68dbb6b7a5b62cd44cacc84569081e068f94a734e25185754c40b01731b269712b2a50ee4146f43e26f1a900d9f46bcbe16ee4a9ddcb96', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/51e8126e-0462-4268-a0f7-55710434de76?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=99f13601e9e45e0d54d8994293d5b64b5319ed17447abb6a3d43340e093deb3b527018649b85d0bce52a45e2379077a60d021867b8571caacef74c53964672aab254dabdd6277ddb2a3ea59728a5a5fba07f32cf947248d602a98d6ccee47a795dca20f88165f88bcaf54a732d8ec27b356f8c8afd6982fb054f27cdfa36c892bad758fcda83cdb06ed5069300ea053402b47cdf2e5ee064135943d08af9c5777afa0dcf57fc0edca41f5bb0452d83833f2410242b266833d7c2efb172fa00a0c7ab966fe536ba250d0b873c0cceaba35097cb85ec6b792ddb9fa496281e643b6fab101034e835cdc54237836de716a3110d6770a74216c20a46cf028cdb9b96', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/4e5c8cf3-6e3c-4049-9fcf-1e5b223fa106?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=977bfdcefba062d432d43565459b41b271a5a02ebf173c9bfb32910ab59c5334b73636c2740d02ad1acb5b79e844b1c07d3612e02083dd5f11ac31e60e961a2d0815c34c3fee32641fd36318ebbc2c2c58fea56a9eef428f6efaecf8cb6132c3d86a0b558d98a61e9320722c8ba2bca6901f38ca6f2700a7bd46c6c093a52688555d4ba0c6afe31fccca0c19a5f59ff8716bc9e95b04663e55cf53e16d31dce81a03f36b949ff9cf77a8d64c2386b85637ab548b9846bce13b352f90a33299a75cdad10cc54726523b7118fa175324cd63a26ce1291361a2b79677f8ace1093b3afff797f86b1a2d0352e32db45a16d9b2487bdfc19a3098fb559ddbce04df46', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/d07fd978-23e6-40cf-ac05-49af8dffede9?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=5707ecc4af51a0a79f97ae874f6d24999537c2e44f4a59a0ca405f5a2b1626dc48fa652a54666b1715d696fec689fd53dd36a7d17555ab0043ef5a841b843145cf746ff5dccbab21fbbfe33f6cfda073ac50a2ac8bb464f08d193f216dc0b9dbfea22f697fd56afcdc3ceaa7d4dbcca61f94e5d1f0e75d72604739f067175cf039a156b29f7b3f4a6664c8a14df72cc68efc4ba95100663e69cb8b513524c576c4961c1290158e580dd943e33831dce8e4d35b5f1d409bc95fede800dfab1dc42c64cf42585a9bc7a48f53bc06d7e5effebccb97b90fb2b0a711f3cf7018a24a3a89cdb5d2461e80261f91eece8d6e7c6183f1499a2f8d41a3cf58673b08b378', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/ba73dc1a-a76f-48e4-8de3-13b47810bd24?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=224f08d4ec68186f064ad6079ce85b33e66bcaa5dabcee3e089c6d9fbdfd614550472a3f8d29e216ad3cda242c1896b38c0f35806da78d78a177f81a35dbd0b3dc975d6ca3f9300d6a38f6fda565689bcbd502fae07800bdba248d165163680e2a0eb10a15acc892ba6b3f7ee2aa7ae0d398fea03bf55094ef0cb9b4ef8f00ab406291a7035b97a42c3e409cb98479921beba882bbe78ee2afda71384c571f275d9b6c2dd46efe6e5b6726c7334446a1e64fcf04f13fcc7596f4ddd60d4e23247b2ddfc30ea4137c938453aab2630eb3e8d3c1a07e17603bec86dd43ad0b9113f840777ba4aeb96f5a307fa9eeaa260a9b9c3da3f8ba574f53bdf56e2ec1319a', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/63595ef2-694a-4a54-9314-5847e29f9ca6?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=5c6390610c53b6c18e8d87c69316c90c53aada13614febb2cba362cc4fa33c7caa84a859f7c010126a97a954874bc6179abd7ad6680a555e4cd2a8e3760b56561b7f5fcaa5c96d37bcbd0b28f98bc9a180e62179cbcb0b36cbc8b97158e68c5049a18592f299bbaabaa6c314a7c054d23a71d49ec0f398a48c2f32fdd3c64c35bea3963a91bef1c0ea828677eadde6ca4f44d028d4f77d26aa69a3071447635f35e4d3393a215d53efb8e8402e5ff636c5ec543ac2e66a4c3fcbfa86d4f6a43bebae6c0e4d14815064a9e6d7ed63e523f1165a2b289994bc21dc7eee80d40618c3246e9017abf46fe88f40cf80f2a8470a765b1f0c1d4a0a4be024140cdb55ce', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/07e4b4cf-8899-4d3a-a2c5-cdd5cb0cd930?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=6e7cff93678860c66cddded8702349baae48b4b20783b2a88f90699f00e4c3f56d52d5295d7fe1f5b7deb22370b8f6ab241017471bea988428804eaac320f822f7f9536b5f1de12f267799a8fc5ff9a8741fbba1a91a9e2d0b954e5e03d19488d6d88fa217904ff0501e60ba920c2e82b426adb24b24ff0e2b9b4e78bd97bf522b2419a2ace07a96927eac09e00ff23396f29b3b623348e060827169d94e8275d59c417d88fcfa093c435724333975818288f5a50beaf76aa6566d8a0b4d691f13151ddcc0e28d4bd20e2265fe61a5135a95c50b86feba6cdfa769fa1d38e8502f961aca2bcec5168cbd1a3fa21018cfc4df77010847bced6de3505de8610c1d', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/bd1d3ed8-db59-4756-8311-882055c9b3ba?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=303b6bba4e4d61da8e48a02d98d80a43cf9c88f6b75c9288a6a0e9f459d0709ed1d62c326fe68d3abd5f7bb05c0d4165984d607155412002e77a7639ab616e7848a18292eb34060378438a4b1fed077b7959dda90a99a17d269f9d1e6bb17fb0dbed3505dc0ee676cd03dca939b8b0006af3b2574ff7b72521b5665f6bae6fbaba4a1e3ebeb71338e3a69bd998de0d1c3e74fc051e9d3b39ee1168695fd9f8f26a7c0ff2c4a8f0133e40641d1b5643bc55eb94b45fa336510ac7575d77821ea1a480afad227f098f122b166ff1f422a549d7953a282541d71adbc9d19c9301386abb8d3d579915657413d0c0f96306ec8122f4beb12f7777236217d43863e77d', 'https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-dicoms-prod/dp2Wf2uuRDg2nHa9CAAnEsltU8d2/7e5fda26-4578-4712-b266-e9ff6689e4a3?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20240705%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240705T114251Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=0bbaee7ed0e0b0c0aac550f071a4ea6428433a112a4ba1c691c3a6e2e183b6ad51edbb7dac15de5abefce8e7f61c116115905e10b2a1549b34230989f9eb3fd4fad66f2d803207c15d52c55b90941a339f34c2e3b4dd397ba9f40b7060c467b94fa097d2e25adc0c8ba751bbf32fec6330ed744879ad27cc91a11a03aacb6ae974c08e149978f54bcc73dd9481d02f1d14f9817ba1b88fbc47d911ddde2cd995b37e1bd408179f36dd82bb224d2a2822761ebad6996fb892c7024399c2bab90c04eecfee1a745f580fbc48d94049516251539707991b411fbc7da0284d14b0c988671502da866a21bda103fcb7b518734def27f024e46920480900a312fa4e32']
#     DCM_path = "D:/PROJECT/encord_T1/dataset/DCM files/"
#     JPG_dir = "D:/PROJECT/encord_T1/dataset/JPG files/"

#     download_and_convert_dicom_parallel(urls, DCM_path, JPG_dir,'sample')
