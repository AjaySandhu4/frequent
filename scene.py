from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService

BUCKET_X = {
    1: -5,
    2: -2,
    3: 1
}
BUCKET_Y = -3

STREAM = [BLUE, GREEN, RED, BLUE, BLUE, GREEN, PURPLE]

class CreateFrequent(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        # self.set_speech_service(RecorderService())
        # self.set_speech_service(
        #     AzureService(voice="en-US-JennyNeural", style="newscast")
        # )
        title = Tex(
                r'The \emph{Frequent} Algorithm',
                font_size=64,
                color=WHITE
            )
        with self.voiceover(text="Hi! Today, we'll be discussing the Frequent algorithm") as tracker:
            self.play(Create(title))
            self.wait(tracker.duration)
        with self.voiceover(text="""
                    A generalization of the famous Boyer-Moore voting algorithm, 
                    it was rediscovered by Demaine, Lopez-Ortiz, and Munro in 2002.     
                    """) as tracker:
            demaine = Tex(r"Demaine, Lopez-Ortiz, and Munro", font_size=24, color=YELLOW)
            demaine.next_to(title, DOWN)
            self.wait(tracker.duration/2)
            self.play(Create(demaine))
        with self.voiceover(text="""More than 20 years after it had been first presented by Misra and Gries.""") as tracker:
            misra_gries = Tex(r"Misra and Gries", font_size=24, color=YELLOW)
            misra_gries.next_to(demaine, 0)
            self.wait(tracker.duration/2)
            self.play(Transform(demaine, misra_gries))
        self.play(Uncreate(title), Uncreate(demaine))
        with self.voiceover(text="""Let us first define the problem. Let a data stream be represented by the sequence S.""") as tracker:
            data_stream_definition = Tex(r"Let a data stream be represented by a sequence $S=(a_1, a_2, \ldots, a_n)$.", font_size=32)
            self.play(Create(data_stream_definition))
        with self.voiceover(text='Our goal is to find the elements that occur more than n over k+1 times.') as tracker:
            data_stream_definition_2 = Tex(r" We want to find the items that, for a given $k$, occur more than $\frac{n}{k+1}$ times.", font_size=32)
            data_stream_definition_2.next_to(data_stream_definition, DOWN)
            self.play(Create(data_stream_definition_2))
        with self.voiceover(text="""This is also known as finding the Heavy Hitters""") as tracker:
            heavy_hitters = Tex(r"We want to find the find the \emph{Heavy Hitters}", font_size=32)
            heavy_hitters.next_to(data_stream_definition_2, 0)
            self.play(Transform(data_stream_definition_2, heavy_hitters))
        with self.voiceover(text="""The catch is in our model, we have limited memory and we can only make one pass through the elements of the stream.""") as tracker:
            self.wait(2)
            limited_memory = Tex(r"We cannot store \emph{all} the elements.", font_size=32)
            limited_memory.next_to(data_stream_definition_2, DOWN)
            self.play(Create(limited_memory))
            self.wait(1)
            one_pass = Tex(r"We can only make \emph{one pass} through the stream.", font_size=32)
            one_pass.next_to(limited_memory, DOWN)
            self.play(Create(one_pass))
        self.play(Uncreate(data_stream_definition), Uncreate(data_stream_definition_2), Uncreate(limited_memory), Uncreate(one_pass)) 
        self.wait(2)
        
        with self.voiceover(text="""The algorithm is beautiful in its simplicity and works as follows.""") as tracker:
            bucket_1 = self.make_bucket()
            bucket_1.move_to([BUCKET_X[1],BUCKET_Y,0])
            bucket_2 = self.make_bucket()
            bucket_2.move_to([BUCKET_X[2],BUCKET_Y,0])
            bucket_3 = self.make_bucket()
            bucket_3.move_to([BUCKET_X[3],BUCKET_Y,0])

            self.play(Create(bucket_1), Create(bucket_2), Create(bucket_3))

            code = '''
                Frequent(k, S):
                    n = 0
                    C = {}
                    for a in S:
                        n += 1
                        if a in C:
                            C[a]++
                        else if |C| < k:
                            C[a] = 1
                        else:
                            for b in C:
                                C[b]--
                                if C[b] == 0:
                                    C = C - {b}
                '''
            rendered_code = Code(code=code, language="Python", line_spacing=0.7, insert_line_no=False, style='emacs')
            rendered_code.shift(UP+RIGHT*4.5).scale(0.7)
            self.play(Create(rendered_code))
        self.wait(2)

        self.voiceover(text="""The algorithm maintains $k$ buckets, each storing a candidate element and a counter. We will go through a small example for $k=3$. For each element in the stream:""")
        with self.voiceover(text="""If the element isn't in any bucket and there exists an empty bucket, place the element in the first vacant bucket and increment its count.""") as tracker:
            first_element = self.make_stream_item(STREAM[0])
            first_element.target.next_to(bucket_1, 0)
            self.play(MoveToTarget(first_element))
            second_element = self.make_stream_item(STREAM[1])
            second_element.target.next_to(bucket_2, 0)
            self.play(MoveToTarget(second_element))
            third_element = self.make_stream_item(STREAM[2])
            third_element.target.next_to(bucket_3, 0)
            self.play(MoveToTarget(third_element))
        with self.voiceover("Else, if a bucket already contains the element, increment the count of that bucket."):
            fourth_element = self.make_stream_item(STREAM[3])
            fourth_element.target.next_to(first_element, UP, 0)
            self.play(MoveToTarget(fourth_element))
            fifth_element = self.make_stream_item(STREAM[4])
            fifth_element.target.next_to(fourth_element, UP, 0)
            self.play(MoveToTarget(fifth_element))
            sixth_element = self.make_stream_item(STREAM[5])
            sixth_element.target.next_to(second_element, UP, 0)
            self.play(MoveToTarget(sixth_element))
        with self.voiceover("Otherwise, if no bucket contains the element and all buckets are full, decrement the count of every bucket."):
            seventh_element = self.make_stream_item(STREAM[6])
            self.wait(2)
            self.play(FadeOut(sixth_element), FadeOut(fifth_element), FadeOut(third_element), FadeOut(seventh_element))
        self.wait(1)
        self.play(Uncreate(bucket_1), Uncreate(bucket_2), Uncreate(bucket_3), Uncreate(rendered_code), Transform(first_element, fourth_element))
        self.remove(fourth_element)
        candidate_1 = first_element
        candidate_2 = second_element
        with self.voiceover("The elements in the buckets at the end of the stream are our Heavy Hitter candidates."):
            stream_group = self.make_stream_group()
            stream_group.shift(UP)
            stream_group.arrange(RIGHT)
            stream_text = Tex(r"Stream:", font_size=48).shift(UP*1.5+LEFT*5)
            candidates_text = Tex(r"Candidates:", font_size=48).shift(DOWN*1.5+LEFT*5)
            stream_group.next_to(stream_text, RIGHT)
            null_candidate = Cross(scale_factor=0.5)
            candidates = VGroup(candidate_1, candidate_2, null_candidate)
            self.play(Create(stream_text), Create(candidates_text), Create(stream_group), candidates.animate.arrange(RIGHT).next_to(candidates_text, RIGHT))
        with self.voiceover("However, you may notice our limitations."):
            n_brace = BraceLabel(stream_group, text="n=8", font_size=32, brace_direction=UP)
            k_brace = BraceLabel(candidates, text="k=3", font_size=32, brace_direction=DOWN)
            self.play(Create(n_brace), Create(k_brace))
            stream_group.sort(submob_func=lambda x: x.get_color().to_hex())
            self.play(stream_group.animate.arrange(RIGHT).next_to(stream_text, RIGHT))
        
        with self.voiceover("First, we have one less candidate than the value of k."):
            self.play(Indicate(null_candidate, run_time = 2))
            
        with self.voiceover("Second, we have a false positive since the green element is not a Heavy Hitter."):   
            greens = VGroup(*[i for i in stream_group if i.get_color() == GREEN])
            greens_brace = Brace(greens, direction=DOWN)
            greens_text_1 = MathTex(r"2 > \frac{n}{k+1}").next_to(greens_brace, DOWN)
            greens_text_2 = MathTex(r"2 > \frac{8}{4}").next_to(greens_brace, DOWN)
            greens_text_3 = MathTex(r"2 > 2").next_to(greens_brace, DOWN)
            greens_text_4 = MathTex(r"\text{False}").next_to(greens_brace, DOWN)
            self.play(Indicate(candidate_2, run_time = 2), Create(greens_brace), Create(greens_text_1))
            self.play(Transform(greens_text_1, greens_text_2))
            self.play(Transform(greens_text_1, greens_text_3))
            self.play(Transform(greens_text_1, greens_text_4))
        self.play(Uncreate(greens_brace), Uncreate(greens_text_1), Uncreate(greens_text_4))
            
            
        with self.voiceover("Nevertheless, as exemplified by the blue element, we can guarantee that the Heavy Hitters are among the candidates."):
            blues = VGroup(*[i for i in stream_group if i.get_color() == BLUE])
            blues_brace = Brace(blues, direction=DOWN)
            blues_text_1 = MathTex(r"3 > \frac{n}{k+1}").next_to(blues_brace, DOWN)
            blues_text_2 = MathTex(r"3 > \frac{8}{4}").next_to(blues_brace, DOWN)
            blues_text_3 = MathTex(r"3 > 2").next_to(blues_brace, DOWN)
            blues_text_4 = MathTex(r"\text{True}").next_to(blues_brace, DOWN)
            self.play(Create(blues_brace), Create(blues_text_1), Indicate(candidate_1))
            self.play(Transform(blues_text_1, blues_text_2))
            self.play(Transform(blues_text_1, blues_text_3))
            self.play(Transform(blues_text_1, blues_text_4))
            self.wait(2)
        
        with self.voiceover("Let us prove that this is always the case."):
            self.play(Uncreate(n_brace), Uncreate(k_brace), Uncreate(stream_text), Uncreate(candidates_text), Uncreate(stream_group), Uncreate(candidates), Uncreate(blues_brace), Uncreate(blues_text_1), Uncreate(blues_text_4))
         
        with self.voiceover("""Let $x$ be an element which occurs more than $n/(k+1)$ times. Let us prove that $x$
                            will always be a candidate at the end of the stream. We will denote its count by $t$"""):
            x = MathTex(r"x", font_size = 48).shift(UP*2)
            self.play(Create(x))
            t_1 = MathTex(r"t > \frac{n}{k+1}").next_to(x, 0)

    def make_bucket(_):
        bucket_right_line = Line(start=[1,-1,0], end=[1,1,0], stroke_width=8)
        bucket_bottom_line = Line(start=[-1,-1,0], end=[1,-1,0], stroke_width=8)
        bucket_left_line = Line(start=[-1,-1,0], end=[-1,1,0], stroke_width=8)
        return VGroup(bucket_right_line, bucket_bottom_line, bucket_left_line).scale(0.7)
    
    def make_stream_item(self, color):
        ball = Circle(radius=0.5, color=color, fill_opacity=1)
        ball.move_to([BUCKET_X[2],5,0])
        ball.generate_target()
        ball.target.move_to([BUCKET_X[2],3,0])
        self.play(Create(ball))
        self.play(MoveToTarget(ball))
        return ball
    
    def make_stream_group(self):
        return VGroup(*[Circle(radius=0.5, color=item_color, fill_opacity=1) for item_color in STREAM])