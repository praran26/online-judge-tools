import unittest

import subprocess
import glob
import os.path
import sys
import hashlib
import shutil
import time
import tempfile

class DownloadTest(unittest.TestCase):

    def snippet_call_download(self, url, files, is_system=False):
        cwd = os.getcwd()
        ojtools = os.path.join( cwd, 'oj' )
        try:
            tempdir = tempfile.mkdtemp()
            os.chdir(tempdir)
            if os.path.exists('test'):
                shutil.rmtree('test')
            cmd = [ ojtools, 'download', url ]
            if is_system:
                cmd += [ '--system' ]
            subprocess.check_call(cmd, stdout=sys.stdout, stderr=sys.stderr)
            result = {}
            for name in os.listdir('test'):
                with open(os.path.join('test', name)) as fh:
                    result[name] = hashlib.md5(fh.buffer.read()).hexdigest()
            self.assertEqual(files, result)
        finally:
            os.chdir(cwd)
            shutil.rmtree(tempdir)

    def test_call_download_hackerrank_beautiful_array(self):
        self.snippet_call_download(
            'https://www.hackerrank.com/contests/hourrank-1/challenges/beautiful-array', {
                'sample-1.in':  'fb3f7e56dac548ce73f9d8e485e5336b',
                'sample-2.out': '897316929176464ebc9ad085f31e7284',
                'sample-2.in':  '6047a07c8defde4d696513d26e871b20',
                'sample-1.out': '6d7fce9fee471194aa8b5b6e47267f03',
            })

    def test_call_download_aoj_DSL_1_A(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A', {
                'sample-1.in':  'cb3a243a13637cddedf245cd0f6eab86',
                'sample-1.out': '29cc7a34bb5a15da3d14ef4a82a4c530',
            })
    def test_call_download_aoj_0100(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0100', {
                'sample-1.in':  '4f0f7b3b0b73c97c5283395edde3dbe8',
                'sample-1.out': '26d3b085a160c028485f3865d07b9192',
            })
    def test_call_download_aoj_1371(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1371', {
                'sample-6.in':  '3521658c02c291ad5a4e5cbaa3cb0260',
                'sample-2.out': 'b026324c6904b2a9cb4b88d6d61c81d1',
                'sample-3.in':  'b9775d52323c110b406d53b9805cee01',
                'sample-3.out': '6d7fce9fee471194aa8b5b6e47267f03',
                'sample-1.out': '897316929176464ebc9ad085f31e7284',
                'sample-5.in':  '0b06c70869a30733379a72e2a8c03758',
                'sample-4.out': 'b026324c6904b2a9cb4b88d6d61c81d1',
                'sample-7.out': '897316929176464ebc9ad085f31e7284',
                'sample-6.out': 'b026324c6904b2a9cb4b88d6d61c81d1',
                'sample-5.out': '897316929176464ebc9ad085f31e7284',
                'sample-2.in':  'f3c536f039be83a4ef0e8f026984d87d',
                'sample-1.in':  '56092c4794d713f93d2bb70a66aa6ca1',
                'sample-4.in':  '318d4b3abfa30cc8fad4b1d34430aea3',
                'sample-7.in':  'dcac31a5a6542979ce45064ab0bfa83d',
            })
    def test_call_download_aoj_2256(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2256&lang=jp', {
                'sample-1.in':  'c89817f1ee0b53209d66abc94e457f7f',
                'sample-1.out': 'b9c2c5761360aad068453f4e64dd5a4e',
            })
    def test_call_download_aoj_2310(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2310&lang=jp', {
                'sample-1.in':  '27ed9e879684b438fa6cc80c4261daf7',
                'sample-1.out': '48a24b70a0b376535542b996af517398',
                'sample-2.in':  'bb84849858ca512e14e071e25120ed78',
                'sample-2.out': '6d7fce9fee471194aa8b5b6e47267f03',
                'sample-3.in':  '4c4ae7fb491ec5c6ad57d9d5711e44a6',
                'sample-3.out': '9ae0ea9e3c9c6e1b9b6252c8395efdc1',
                'sample-4.in':  'ad1109594a97eabe9bee60a743006de7',
                'sample-4.out': '84bc3da1b3e33a18e8d5e1bdd7a18d7a',
                'sample-5.in':  'b80447e0bc0c4ecc6fb3001b6a4e79f6',
                'sample-5.out': 'c30f7472766d25af1dc80b3ffc9a58c7',
            })
    def test_call_download_aoj_2511(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2511', {
                'sample-1.in':  '0483a0080de977d5e1db1ab87eae3fa9',
                'sample-1.out': '346ce6367eff6bb3c9915601f2ae1e75',
            })

    def test_call_download_aoj_system_ITP1_1_B(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_B', {
                '1.in':  'b026324c6904b2a9cb4b88d6d61c81d1',
                '1.out': 'b026324c6904b2a9cb4b88d6d61c81d1',
                '2.in':  '6d7fce9fee471194aa8b5b6e47267f03',
                '2.out': '66a7c1d5cb75ef2542524d888fd32f4a',
                '3.in':  '9caff0735bc6e80121cedcb98ca51821',
                '3.out': 'fef5f767008b27f5c3801382264f46ef',
                '4.in':  '919d117956d3135c4c683ff021352f5c',
                '4.out': 'b39ffd5aa5029d696193c8362dcb1d19',
            }, is_system=True)
    def test_call_download_aoj_system_1169(self):
        self.snippet_call_download(
            'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1169&lang=jp', {
                '1.in':  'f0ecaede832a038d0e940c2c4d0ab5e5',
                '1.out': '8d2f7846dc2fc10ef37dcb548635c788',
            }, is_system=True)

    def test_call_download_yukicoder_no_9002(self):
        self.snippet_call_download(
            'http://yukicoder.me/problems/no/9002', {
                'sample-1.in':  'b026324c6904b2a9cb4b88d6d61c81d1',
                'sample-2.out': 'a403d4dbee7bd783539da3efa43c4399',
                'sample-2.in':  '5b6b41ed9b343fed9cd05a66d36650f0',
                'sample-1.out': 'b026324c6904b2a9cb4b88d6d61c81d1',
            })
    def test_call_download_yukicoder_100(self):
        self.snippet_call_download(
            'http://yukicoder.me/problems/100', {
                'sample-3.out': '63a98316f78c5127e702db8fbea612a6',
                'sample-2.in':  '3b6feb4b7d767c8e7314f59a1749d544',
                'sample-2.out': '9f4c0b1fca5cb6f886aa2e54442b1e1b',
                'sample-3.in':  'c12ec911666a5d65bf53e234291e402c',
                'sample-1.in':  'c8a8eeb947c8a1d6700d6f7fd151cb00',
                'sample-1.out': '3bb50ff8eeb7ad116724b56a820139fa',
            })
    def test_call_download_yukicoder_no_104(self):
        self.snippet_call_download(
            'http://yukicoder.me/problems/no/104', {
                'sample-3.out': '89c2e8d24975544fd508992593bd4556',
                'sample-2.in':  '82e80aeb6240ed14d8a0f8df1bc4ab19',
                'sample-2.out': '2737b49252e2a4c0fe4c342e92b13285',
                'sample-3.in':  '802bd42d2ee2af1b0f2165ba526bd1f8',
                'sample-1.in':  'bc6bccbab69279fd7c28fc71654e57bc',
                'sample-4.in':  '68b329da9893e34099c7d8ad5cb9c940',
                'sample-1.out': '1dcca23355272056f04fe8bf20edfce0',
                'sample-4.out': 'b026324c6904b2a9cb4b88d6d61c81d1',
            })
    def test_call_download_yukicoder_no_400(self):
        self.snippet_call_download(
            'http://yukicoder.me/problems/no/400', {
                'sample-3.out': '9c9eb7aca96d568294f752ecd6867cbe',
                'sample-2.in':  '60650122d9941f5b816451ca15d9eff9',
                'sample-2.out': '90e2a41ae5ea1f30688dcf72ba806b17',
                'sample-3.in':  '9c9eb7aca96d568294f752ecd6867cbe',
                'sample-1.in':  '04b3f6b553cb51fcc486e0a8888c79eb',
                'sample-4.in':  '787786577e5cb219fd38409b5cb7b933',
                'sample-1.out': '3e1ce07401b37846f4d6aab1efbe771b',
                'sample-4.out': '60f3f85857568779dbd10bc4fc506f35',
            })
    def test_call_download_yukicoder_no_260(self):
        self.snippet_call_download(
            'http://yukicoder.me/problems/no/260/', {
                'sample-3.out': '15aac79ea3df9c684a6472d156241987',
                'sample-2.in':  'fdd3527dacad0f949c31f7c4e7fd0c12',
                'sample-2.out': '49a6957c6e2e1c5ce89cde8898949ae1',
                'sample-3.in':  '0ffaa5e4f1ec8fe18e25698504d659ae',
                'sample-1.in':  'b16aaad0c06f931e38ad651115b73f56',
                'sample-1.out': '90e2a51705594d033a3abe9d77b2b7ad',
            })

    def test_call_download_anarchygolf_the_b_programming_language(self):
        self.snippet_call_download(
            'http://golf.shinh.org/p.rb?The+B+Programming+Language', {
                'sample-3.out': 'fcbee46b3b888607abe720d598c75b17',
                'sample-2.in':  '810d1189284ef048fc30f80ba7a22c6d',
                'sample-2.out': 'd4e62449830b2a986024d914b194f129',
                'sample-3.in':  '7361217616875a437a3d6b41612dacbb',
                'sample-1.in':  '3de90f793f16fad76da1527e09b8e528',
                'sample-1.out': 'f67b46b3c53308d8a6414b20092a2220',
            })
    def test_call_download_anarchygolf_simple_language(self):
        self.snippet_call_download(
            'http://golf.shinh.org/p.rb?simple+language', {
                'sample-3.out': 'c4211571f7a72cfad092b4dac7b15144',
                'sample-2.in':  '10e10b554ef9bc07d56a514d2f6dab26',
                'sample-2.out': '48a24b70a0b376535542b996af517398',
                'sample-3.in':  'f201f3f6606e56f561f8452c9a60210b',
                'sample-1.in':  '9b3c9ece5285bb1bcd1164cec8aa4243',
                'sample-1.out': '48a24b70a0b376535542b996af517398',
            })
    def test_call_download_anarchygolf_hello_world(self):
        self.snippet_call_download(
            'http://golf.shinh.org/p.rb?hello+world', {
                'sample-1.in':  'd41d8cd98f00b204e9800998ecf8427e',
                'sample-1.out': '746308829575e17c3331bbcb00c0898b',
            })
    def test_call_download_anarchygolf_momomo(self):
        self.snippet_call_download(
            'http://golf.shinh.org/p.rb?momomo', {
                'sample-1.in':  '281e30fff54f179881c67c4d0564633e',
                'sample-1.out': 'd67adc236dd84fd82fb4598922d5cf32',
            })

    def test_call_download_codeforces_problemset_700_b(self):
        self.snippet_call_download(
            'http://codeforces.com/problemset/problem/700/B', {
                'sample-1.in':  '1f38b0f27f4b0005e5409e834ff59166',
                'sample-2.out': '7c5aba41f53293b712fd86d08ed5b36e',
                'sample-2.in':  '8a8c08b2901d4cfca41ad0703dfa718e',
                'sample-1.out': '9ae0ea9e3c9c6e1b9b6252c8395efdc1',
            })
    def test_call_download_codeforces_contest_538_h(self):
        self.snippet_call_download(
            'http://codeforces.com/contest/538/problem/H', {
                'sample-1.in':  'c8483ca371b414e911ccbecf239beed6',
                'sample-2.out': '87a45b8adc25c7bf37eaa25b530de79c',
                'sample-2.in':  'afa0c8b2336e798b5f29a200a18432d1',
                'sample-1.out': '166a3645f3c31595526624ce003b41fc',
            })
    def test_call_download_codeforces_gym_101021_a(self):
        self.snippet_call_download(
            'http://codeforces.com/gym/101021/problem/A', {
                'sample-1.in':  '4dfb06c20503a3f0dbe0fb29dd52d304',
                'sample-2.out': '614a0c8025f8bbcf46b8ba0ff9fd61d1',
                'sample-2.in':  'dcfe1f14721a0e141c2e31adeebe7a53',
                'sample-1.out': '45778e8e2d350841cf68711ece5cb9e1',
            })

    def test_call_download_atcoder_abc001_1(self):
        self.snippet_call_download(
            'http://abc001.contest.atcoder.jp/tasks/abc001_1', {
                'sample-3.out': '0735cf297f0e794bcfa7515f25d189fc',
                'sample-2.in':  'c4da2b805df8425bccc182ad4db8422a',
                'sample-2.out': '897316929176464ebc9ad085f31e7284',
                'sample-3.in':  'e49623ffecc4347eaa5b3e235d5752bd',
                'sample-1.in':  'ec7562c808cc6c106a4d62d212daefd9',
                'sample-1.out': '1dcca23355272056f04fe8bf20edfce0',
            })
    def test_call_download_atcoder_icpc2013spring_a(self):
        self.snippet_call_download(
            'http://jag2013spring.contest.atcoder.jp/tasks/icpc2013spring_a', {
                'sample-3.out': 'e14b420b7266f69a2b2b457f3bbec804',
                'sample-5.out': '3ae2ea0c3867b219ef54d914437e76be',
                'sample-2.in':  '9121f567aad63b98115e8c793a0e2e72',
                'sample-2.out': '3ae2ea0c3867b219ef54d914437e76be',
                'sample-3.in':  'd797a450bb87f8000cda4b45991fc894',
                'sample-1.in':  'b0fba7805dabe2ee3cf299d97a2f6ec2',
                'sample-4.in':  '0ef2e8b0c0a59602c1b4390b58948498',
                'sample-1.out': '3ae2ea0c3867b219ef54d914437e76be',
                'sample-5.in':  '9c8befefed86e886539c9baa85e6724a',
                'sample-4.out': 'e14b420b7266f69a2b2b457f3bbec804',
            })
    def test_call_download_atcoder_arc035_a(self):
        self.snippet_call_download(
            'http://arc035.contest.atcoder.jp/tasks/arc035_a', {
                'sample-3.out': '21da93069c74dfbc3c02999e8f27a712',
                'sample-2.in':  '0bee89b07a248e27c83fc3d5951213c1',
                'sample-2.out': '19541a2746e08a6b8f5145bdbaa23e45',
                'sample-3.in':  '2f597205eff28f4f3561934953478a3c',
                'sample-1.in':  '8911d4ca8a5462050cd9cad1984a86e7',
                'sample-4.in':  '2bb6aed5111ef9726bcf6eef982ff32b',
                'sample-1.out': '21da93069c74dfbc3c02999e8f27a712',
                'sample-4.out': '21da93069c74dfbc3c02999e8f27a712',
            })
    def test_call_download_atcoder_arc001_1(self):
        self.snippet_call_download(
            'http://arc001.contest.atcoder.jp/tasks/arc001_1', {
                'sample-3.out': 'b7ca7cc0db40e50e6575025472fcbeab',
                'sample-2.in':  '178aa146bf65370f626f5b0dc63d6d32',
                'sample-2.out': 'cee9c772621fa0919c3f411e591ae81b',
                'sample-3.in':  '57b9c678fa47979fa44d69bbe60ffadb',
                'sample-1.in':  'ffa1fbc1d14328005da451b67c65d35a',
                'sample-1.out': '3e49d46d6c574dc91c9736436eb06d0a',
            })
    def test_call_download_atcoder_agc001_a(self):
        self.snippet_call_download(
            'http://agc001.contest.atcoder.jp//////tasks//////agc001_a//////?hoge=fuga#piyo', {
                'sample-1.in':  '1aba94ea0ab5e89d4a11b3724bdeb5cc',
                'sample-2.out': '615010a656a5bb29d1898f163619611f',
                'sample-2.in':  'd38a35564e44aa124f04f5088e7203d9',
                'sample-1.out': '6d7fce9fee471194aa8b5b6e47267f03',
            })
    def test_call_download_atcoder_abc073_a(self):
        self.snippet_call_download(
            'https://beta.atcoder.jp/contests/abc073/tasks/abc073_a', {
                'sample-1.in':  '22cab69bca05d296a2d779a52cdee643',
                'sample-1.out': '3ae2ea0c3867b219ef54d914437e76be',
                'sample-2.in':  '8faff61bc1198cc6bdc19adafc27fc82',
                'sample-2.out': 'e14b420b7266f69a2b2b457f3bbec804',
                'sample-3.in':  '80ad60f95c32a3f6e413b5bb7c094e99',
                'sample-3.out': '3ae2ea0c3867b219ef54d914437e76be',
            })
    def test_call_download_atcoder_ddcc2017_qual_a(self):
        self.snippet_call_download(
            'https://beta.atcoder.jp/contests/ddcc2017-qual/tasks/ddcc2017_qual_a', {
                'sample-1.in':  '79b0c0aac7451776e794095b2c596422',
                'sample-1.out': '3ae2ea0c3867b219ef54d914437e76be',
                'sample-2.in':  'ae5b468c7707a1f3d36c49b1fe2ef850',
                'sample-2.out': 'e14b420b7266f69a2b2b457f3bbec804',
                'sample-3.in':  'ed5d34c74e59d16bd6d5b3683db655c3',
                'sample-3.out': 'e14b420b7266f69a2b2b457f3bbec804',
            })

    def test_call_download_csacademy_k_swap(self):
        self.snippet_call_download(
            'https://csacademy.com/contest/round-39/task/k-swap/', {
                'sample-1.in':  '2ce34946200aa66529dbc96b411e2450',
                'sample-1.out': '78c6d00be497cd50311743df6c8de3ea',
                'sample-2.in':  '65625b1f27b94fc2c5b6532a18f93070',
                'sample-2.out': '16324a714d2c6f4f9feefe65f0784094',
                'sample-3.in':  '8e92bd4fb348c40f78a13c56a1f5a937',
                'sample-3.out': 'c31f209a3d0412a16c4b93e4ee060b54',
            })
    def test_call_download_csacademy_unfair_game(self):
        self.snippet_call_download(
            'https://csacademy.com/contest/archive/task/unfair_game/', {
                'sample-1.in':  '57cce69a08e8dd833a9f9aa3b6d13a40',
                'sample-1.out': '367764329430db34be92fd14a7a770ee',
                'sample-2.in':  '46b87e796b61eb9b8970e83c93a02809',
                'sample-2.out': 'eb844645e8e61de0a4cf4b991e65e63e',
            })


if __name__ == '__main__':
    unittest.main()
