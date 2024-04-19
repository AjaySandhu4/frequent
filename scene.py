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
        # title = Tex(
        #         r'The \emph{Frequent} Algorithm',
        #         font_size=64,
        #         color=WHITE
        #     )
        # with self.voiceover(text="Hi! Today, we'll be discussing the Frequent algorithm") as tracker:
        #     self.play(Create(title))
        #     self.wait(tracker.duration)
        # with self.voiceover(text="""
        #             A generalization of the famous Boyer-Moore voting algorithm, 
        #             it was rediscovered by Demaine, Lopez-Ortiz, and Munro in 2002.     
        #             """) as tracker:
        #     demaine = Tex(r"Demaine, Lopez-Ortiz, and Munro", font_size=24, color=YELLOW)
        #     demaine.next_to(title, DOWN)
        #     self.wait(tracker.duration/2)
        #     self.play(Create(demaine))
        # with self.voiceover(text="""More than 20 years after it had been first presented by Misra and Gries.""") as tracker:
        #     misra_gries = Tex(r"Misra and Gries", font_size=24, color=YELLOW)
        #     misra_gries.next_to(demaine, 0)
        #     self.wait(tracker.duration/2)
        #     self.play(Transform(demaine, misra_gries))
        # self.play(Uncreate(title), Uncreate(demaine))
        # with self.voiceover(text="""Let us first define the problem. Let a data stream be represented by the sequence S.""") as tracker:
        #     data_stream_definition = Tex(r"Let a data stream be represented by a sequence $S=(a_1, a_2, \ldots, a_n)$.", font_size=32)
        #     self.play(Create(data_stream_definition))
        # with self.voiceover(text='Our goal is to find the elements that occur more than n over k+1 times.') as tracker:
        #     data_stream_definition_2 = Tex(r" We want to find the items that, for a given $k$, occur more than $\frac{n}{k+1}$ times.", font_size=32)
        #     data_stream_definition_2.next_to(data_stream_definition, DOWN)
        #     self.play(Create(data_stream_definition_2))
        # with self.voiceover(text="""This is also known as finding the Heavy Hitters""") as tracker:
        #     heavy_hitters = Tex(r"We want to find the find the \emph{Heavy Hitters}", font_size=32)
        #     heavy_hitters.next_to(data_stream_definition_2, 0)
        #     self.play(Transform(data_stream_definition_2, heavy_hitters))
        # with self.voiceover(text="""The catch is in our model, we have limited memory and we can only make one pass through the elements of the stream.""") as tracker:
        #     self.wait(2)
        #     limited_memory = Tex(r"We cannot store \emph{all} the elements.", font_size=32)
        #     limited_memory.next_to(data_stream_definition_2, DOWN)
        #     self.play(Create(limited_memory))
        #     self.wait(1)
        #     one_pass = Tex(r"We can only make \emph{one pass} through the stream.", font_size=32)
        #     one_pass.next_to(limited_memory, DOWN)
        #     self.play(Create(one_pass))
        # self.play(Uncreate(data_stream_definition), Uncreate(data_stream_definition_2), Uncreate(limited_memory), Uncreate(one_pass)) 
        # self.wait(2)
        
        # with self.voiceover(text="""The algorithm is beautiful in its simplicity and works as follows.""") as tracker:
        #     bucket_1 = self.make_bucket()
        #     bucket_1.move_to([BUCKET_X[1],BUCKET_Y,0])
        #     bucket_2 = self.make_bucket()
        #     bucket_2.move_to([BUCKET_X[2],BUCKET_Y,0])
        #     bucket_3 = self.make_bucket()
        #     bucket_3.move_to([BUCKET_X[3],BUCKET_Y,0])

        #     self.play(Create(bucket_1), Create(bucket_2), Create(bucket_3))

        #     code = '''
        #         Frequent(k, S):
        #             n = 0
        #             C = {}
        #             for a in S:
        #                 n += 1
        #                 if a in C:
        #                     C[a]++
        #                 else if |C| < k:
        #                     C[a] = 1
        #                 else:
        #                     for b in C:
        #                         C[b]--
        #                         if C[b] == 0:
        #                             C = C - {b}
        #         '''
        #     rendered_code = Code(code=code, language="Python", line_spacing=0.7, insert_line_no=False, style='emacs')
        #     rendered_code.shift(UP+RIGHT*4.5).scale(0.7)
        #     self.play(Create(rendered_code))
        # self.wait(2)

        # self.voiceover(text="""The algorithm maintains $k$ buckets, each storing a candidate element and a counter. We will go through a small example for $k=3$. For each element in the stream:""")
        # with self.voiceover(text="""If the element isn't in any bucket and there exists an empty bucket, place the element in the first vacant bucket and increment its count.""") as tracker:
        #     first_element = self.make_stream_item(STREAM[0])
        #     first_element.target.next_to(bucket_1, 0)
        #     self.play(MoveToTarget(first_element))
        #     second_element = self.make_stream_item(STREAM[1])
        #     second_element.target.next_to(bucket_2, 0)
        #     self.play(MoveToTarget(second_element))
        #     third_element = self.make_stream_item(STREAM[2])
        #     third_element.target.next_to(bucket_3, 0)
        #     self.play(MoveToTarget(third_element))
        # with self.voiceover("Else, if a bucket already contains the element, increment the count of that bucket."):
        #     fourth_element = self.make_stream_item(STREAM[3])
        #     fourth_element.target.next_to(first_element, UP, 0)
        #     self.play(MoveToTarget(fourth_element))
        #     fifth_element = self.make_stream_item(STREAM[4])
        #     fifth_element.target.next_to(fourth_element, UP, 0)
        #     self.play(MoveToTarget(fifth_element))
        #     sixth_element = self.make_stream_item(STREAM[5])
        #     sixth_element.target.next_to(second_element, UP, 0)
        #     self.play(MoveToTarget(sixth_element))
        # with self.voiceover("Otherwise, if no bucket contains the element and all buckets are full, decrement the count of every bucket."):
        #     seventh_element = self.make_stream_item(STREAM[6])
        #     self.wait(2)
        #     self.play(FadeOut(sixth_element), FadeOut(fifth_element), FadeOut(third_element), FadeOut(seventh_element))
        # self.wait(1)
        # self.play(Uncreate(bucket_1), Uncreate(bucket_2), Uncreate(bucket_3), Uncreate(rendered_code), Transform(first_element, fourth_element))
        # self.remove(fourth_element)
        # candidate_1 = first_element
        # candidate_2 = second_element
        # with self.voiceover("The elements in the buckets at the end of the stream are our Heavy Hitter candidates."):
        #     stream_group = self.make_stream_group()
        #     stream_group.shift(UP)
        #     stream_group.arrange(RIGHT)
        #     stream_text = Tex(r"Stream:", font_size=48).shift(UP*1.5+LEFT*5)
        #     candidates_text = Tex(r"Candidates:", font_size=48).shift(DOWN*1.5+LEFT*5)
        #     stream_group.next_to(stream_text, RIGHT)
        #     null_candidate = Cross(scale_factor=0.5)
        #     candidates = VGroup(candidate_1, candidate_2, null_candidate)
        #     self.play(Create(stream_text), Create(candidates_text), Create(stream_group), candidates.animate.arrange(RIGHT).next_to(candidates_text, RIGHT))
        # with self.voiceover("However, you may notice our limitations."):
        #     n_brace = BraceLabel(stream_group, text="n=8", font_size=32, brace_direction=UP)
        #     k_brace = BraceLabel(candidates, text="k=3", font_size=32, brace_direction=DOWN)
        #     self.play(Create(n_brace), Create(k_brace))
        #     stream_group.sort(submob_func=lambda x: x.get_color().to_hex())
        #     self.play(stream_group.animate.arrange(RIGHT).next_to(stream_text, RIGHT))
        
        # with self.voiceover("First, we have one less candidate than the value of k."):
        #     self.play(Indicate(null_candidate, run_time = 2))
            
        # with self.voiceover("Second, we have a false positive since the green element is not a Heavy Hitter."):   
        #     greens = VGroup(*[i for i in stream_group if i.get_color() == GREEN])
        #     greens_brace = Brace(greens, direction=DOWN)
        #     greens_text_1 = MathTex(r"2 > \frac{n}{k+1}").next_to(greens_brace, DOWN)
        #     greens_text_2 = MathTex(r"2 > \frac{8}{4}").next_to(greens_brace, DOWN)
        #     greens_text_3 = MathTex(r"2 > 2").next_to(greens_brace, DOWN)
        #     greens_text_4 = MathTex(r"\text{False}").next_to(greens_brace, DOWN)
        #     self.play(Indicate(candidate_2, run_time = 2), Create(greens_brace), Create(greens_text_1))
        #     self.play(Transform(greens_text_1, greens_text_2))
        #     self.play(Transform(greens_text_1, greens_text_3))
        #     self.play(Transform(greens_text_1, greens_text_4))
        # self.play(Uncreate(greens_brace), Uncreate(greens_text_1), Uncreate(greens_text_4))
            
            
        # with self.voiceover("Nevertheless, as exemplified by the blue element, we can guarantee that the Heavy Hitters are among the candidates."):
        #     blues = VGroup(*[i for i in stream_group if i.get_color() == BLUE])
        #     blues_brace = Brace(blues, direction=DOWN)
        #     blues_text_1 = MathTex(r"3 > \frac{n}{k+1}").next_to(blues_brace, DOWN)
        #     blues_text_2 = MathTex(r"3 > \frac{8}{4}").next_to(blues_brace, DOWN)
        #     blues_text_3 = MathTex(r"3 > 2").next_to(blues_brace, DOWN)
        #     blues_text_4 = MathTex(r"\text{True}").next_to(blues_brace, DOWN)
        #     self.play(Create(blues_brace), Create(blues_text_1), Indicate(candidate_1))
        #     self.play(Transform(blues_text_1, blues_text_2))
        #     self.play(Transform(blues_text_1, blues_text_3))
        #     self.play(Transform(blues_text_1, blues_text_4))
        #     self.wait(2)
        
        # with self.voiceover("Let us prove that this is always the case."):
        #     self.play(Uncreate(n_brace), Uncreate(k_brace), Uncreate(stream_text), Uncreate(candidates_text), Uncreate(stream_group), Uncreate(candidates), Uncreate(blues_brace), Uncreate(blues_text_1), Uncreate(blues_text_4))
         
        # with self.voiceover("""Let $x$ be an element which occurs more than $n/(k+1)$ times, where t denotes its count. Let us prove that $x$
        #                     will always be a candidate at the end of the stream."""):
        #     x = MathTex(r"x", font_size = 48)
        #     self.play(Create(x))
        #     self.wait(2)
        #     t = MathTex(r"t", font_size = 48)
        #     threshold = MathTex(r">\frac{n}{k+1}", font_size = 48)
        #     t_1 = VGroup(t, threshold).arrange(RIGHT).next_to(x, 0)
        #     self.play(ReplacementTransform(x, t_1))
        # with self.voiceover("""Now, let $f$ represent the number of times in which when $x$ is read, we do not have a bucket containing $x$ and
        #                     all the buckets are full. This means that in each of these occurences, we decrement all the counters in the buckets."""):
        #     f = MathTex(r"f", font_size = 48).next_to(t_1, UP*3)
        #     self.play(Create(f))
        # with self.voiceover("""Next, let i represent the number of times in which when $x$ is read, we either have a bucket containing $x$ or there is an empty bucket.
        #                     In each of these occurences, x causes its own bucket to be incremented."""):
        #     i = MathTex(r"i", font_size = 48).next_to(f, RIGHT)
        #     self.play(f.animate.shift(LEFT),Create(i))
        # with self.voiceover("""Observe that these are the only two possibilities when x is read. Thus, we can say that t is the sum of these counts"""):
        #     plus = MathTex(r"+")
        #     equal = MathTex(r"=")
        #     t_sum = VGroup(f, plus, i, equal, t, threshold)
        #     self.play(t_sum.animate.arrange(RIGHT))
        #     self.wait(2)
        #     t_sum.remove(equal, t)
        #     self.play(t_sum.animate.arrange(RIGHT))
        #     self.wait(2)
        # with self.voiceover("""Next, let d be the total number of times that a bucket containing x is decremented. Since a counter never goes below zero, we 
        #                     can say that d is at most i. Furthermore, if d is equal to i, that means that x is not one of our candidates since it wouldnt
        #                     occupy one of the buckets at the end of the stream. In order to reach a contradiction, let us assume that this is the case."""):
        #     d = MathTex(r"d", font_size = 48).next_to(t_sum, UP*3)
        #     self.play(Create(d))
        #     self.wait(2)
        #     i_2 = MathTex(r"i", font_size = 48)
        #     d_inequality = VGroup(d, MathTex(r"\leq"), i_2)
        #     self.play(d_inequality.animate.arrange(RIGHT).next_to(d, 0))
        #     self.wait(2)
        #     d_equality = VGroup(d, MathTex(r"="), i_2).arrange(RIGHT).next_to(t_sum, UP*3)
        #     self.play(ReplacementTransform(d_inequality, d_equality))
        #     self.wait(2)
        # with self.voiceover("Then, we substitute i for d:"):
        #     t_sum.remove(i, threshold)
        #     t_sum.add(d, threshold)
        #     d_equality.remove(d)
        #     self.play(t_sum.animate.arrange(RIGHT), Uncreate(d_equality))
        #     self.wait(2)
        # with self.voiceover("Then, multiplying both sides by k+1 gives us this:"):
        #     inequality1 = MathTex(r"(f + d)(k+1) > n")
        #     self.play(ReplacementTransform(t_sum, inequality1))
        #     self.wait(2)

        # with self.voiceover("""Now for the key oberservation. The values of d and f represent times in which the buckets are all full and are all
        #                     decremented. The fact we can decrement a bucket represents that an element must have incremented that bucket in the past.
        #                     Moreover, each of these buckets contain a distinct element and we also have the new element in the stream that caused the decrements.
        #                     This means that for each of these d + f decrements, we can associate k+1 distinct occurences of elements in the stream."""):
        #     inequality2 = MathTex(r"(f + d)(k+1)").next_to(inequality1, UP * 2)
        #     self.play(Create(inequality2), inequality1.animate.shift(DOWN))
        #     self.wait(2)   
        # with self.voiceover('Since there are n total elements in the stream, it must be the case that the number of these associated elements is at most n.'):
        #     inequality2.add(MathTex(r"\leq n"))
        #     self.play(inequality2.animate.arrange(RIGHT).next_to(inequality1, UP * 4))
        #     self.wait(2)
        # with self.voiceover("""But wait a second. This is a contradiction. This means that our assumption was wrong and that d must be strictly less than i.
        #                     This then means the bucket containing x must be decremented less than the number of times it was incremented.
        #                     Therefore, x must be a candidate at the end of the stream.
        #                     """):
        #     contradiction = self.contradiction_arrow()
        #     self.play(Create(contradiction))
        #     self.wait(2)
        #     self.play(Uncreate(contradiction), Uncreate(inequality1), Uncreate(inequality2))

        with self.voiceover("""Now, I have been purposefully vague about the implemention. Due to the nature of data streams, we usually have very little time to process each element.
                            This means that operations such as decrementing the counter of every bucket should ideally be done in constant time. Fortunately, Demaine et al. provide 
                            a data structure that can achieve this for us. It consists of maintaining groups of counters, where each group is associated with a count value and are connected together
                            by a doubly linked list. Furthermore, each group does not store its own count value, but rather the difference between its count value and the count value of the previous group.
                            This is known as a differential encoding. Let us see how this works."""):
            first_group_text = MathTex(r"\text{Value}=0")
            first_group_rec = SurroundingRectangle(first_group_text, corner_radius=0.5, buff=0.5, color=WHITE)
            first_group = VGroup(first_group_text, first_group_rec).scale(0.8)
            

            counter_1_cross = Cross(scale_factor=0.4)
            counter_1_rec = SurroundingRectangle(counter_1_cross, buff=0.2, color=WHITE)
            
            counter_2_cross = Cross(scale_factor=0.4)
            counter_2_rec = SurroundingRectangle(counter_2_cross, buff=0.2, color=WHITE)
            
            counter_3_cross = Cross(scale_factor=0.4)
            counter_3_rec = SurroundingRectangle(counter_3_cross, buff=0.2, color=WHITE)


            counter_1 = VGroup(counter_1_cross, counter_1_rec)
            counter_1.next_to(first_group, DOWN*3+LEFT)
            counter_2 = VGroup(counter_2_cross, counter_2_rec)
            counter_2.next_to(first_group, DOWN*3)
            counter_3 = VGroup(counter_3_cross, counter_3_rec)
            counter_3.next_to(first_group, DOWN*3+RIGHT)
            
            counter_1_next_arrow = CurvedArrow(start_point=counter_1_rec.get_right(), end_point=counter_2_rec.get_left(), angle=-PI/2, color=WHITE)
            counter_1_next_arrow.tip.height = 0.3
            counter_1.add(counter_1_next_arrow)
            counter_2_prev_arrow = CurvedArrow(start_point=counter_2_rec.get_left(), end_point=counter_1_rec.get_right(), angle=-PI/2, color=WHITE)
            counter_2_prev_arrow.tip.height = 0.3
            counter_2_next_arrow = CurvedArrow(start_point=counter_2_rec.get_right(), end_point=counter_3_rec.get_left(), angle=-PI/2, color=WHITE)
            counter_2_next_arrow.tip.height = 0.3
            
            counter_2.add(counter_2_prev_arrow, counter_2_next_arrow)
            counter_2.add(counter_2_prev_arrow)

            counter_3_prev_arrow = CurvedArrow(start_point=counter_3_rec.get_left(), end_point=counter_2_rec.get_right(), angle=-PI/2, color=WHITE)
            counter_3_prev_arrow.tip.height = 0.3
            counter_3.add(counter_3_prev_arrow)

            counter_1_group_arrow = CurvedArrow(start_point=counter_1_rec.get_top(), end_point=first_group_rec.get_corner(DL)+UP*0.1+RIGHT*0.1, angle=-PI/2, color=WHITE)
            counter_1_group_arrow.tip.height = 0.3
            counter_1.add(counter_1_group_arrow)
            counter_2_group_arrow = CurvedArrow(start_point=counter_2_rec.get_top(), end_point=first_group_rec.get_bottom(), angle=0, color=WHITE)
            counter_2_group_arrow.tip.height = 0.3
            counter_2.add(counter_2_group_arrow)
            counter_3_group_arrow = CurvedArrow(start_point=counter_3_rec.get_top(), end_point=first_group_rec.get_corner(DR)+UP*0.1+LEFT*0.1, angle=PI/2, color=WHITE)
            counter_3_group_arrow.tip.height = 0.3
            counter_3.add(counter_3_group_arrow)

            first_group_arrow_down = CurvedArrow(start_point=first_group_rec.get_corner(DL)+UP*0.1+RIGHT*0.1, end_point=counter_1_rec.get_top(), angle=0, color=WHITE)
            first_group_arrow_down.tip.height = 0.3
            first_group.add(first_group_arrow_down)

            first_group.add(counter_1, counter_2, counter_3)
            # counter_dict = {}
            # counter_dict[1] = {
            #     "item": counter_1_cross,
            #     "rectangle": counter_1_rec,
            #     "group_arrow": CurvedArrow(start_point=counter_1.get_center(), end_point=first_group.get_center(), angle=PI/2, color=WHITE),
            #     "next_arrow": 
                
            # }
            self.play(Create(first_group))


            # first ball into counter
            ball_1 = self.make_stream_ball_2(STREAM[0])
            ball_1.generate_target()
            ball_1.target.move_to(counter_1_cross.get_center())
            self.play(MoveToTarget(ball_1))
            self.play(ReplacementTransform(counter_1_cross, ball_1))
            # counter_1.add(ball_1)

            #### splitting first group ####
            second_group_text = MathTex(r"\text{Diff}=1")
            second_group_rec = SurroundingRectangle(second_group_text, corner_radius=0.5, buff=0.5, color=WHITE)
            second_group = VGroup(second_group_text, second_group_rec).scale(0.8)
            second_group.shift(RIGHT*2)
            second_group.add(counter_1)
            counter_1.remove(counter_1_next_arrow, counter_1_group_arrow)
            counter_1.next_to(second_group_rec, DOWN*3)
            counter_1_group_arrow = CurvedArrow(start_point=counter_1_rec.get_top(), end_point=second_group_rec.get_bottom(), angle=PI/2, color=WHITE)
            counter_1_group_arrow.tip.height = 0.3
            counter_1.add(counter_1_group_arrow)
            second_group_arrow_down = CurvedArrow(start_point=second_group_rec.get_bottom(), end_point=counter_1_rec.get_top(), angle=PI/2, color=WHITE)
            second_group_arrow_down.tip.height = 0.3
            second_group.add(second_group_arrow_down)
            first_group.remove(counter_1)

            counter_2.shift(LEFT)
            counter_2.remove(counter_2_prev_arrow, counter_2_group_arrow)
            counter_2_group_arrow = CurvedArrow(start_point=counter_2_rec.get_top(), end_point=first_group_rec.get_bottom(), angle=PI/4, color=WHITE)
            counter_2_group_arrow.tip.height = 0.3
            counter_2.add(counter_2_group_arrow)
            counter_3.shift(LEFT)
            counter_3.remove(counter_3_group_arrow)
            counter_3_group_arrow = CurvedArrow(start_point=counter_3_rec.get_top(), end_point=first_group_rec.get_bottom(), angle=0, color=WHITE)
            counter_3_group_arrow.tip.height = 0.3
            counter_3.add(counter_3_group_arrow)

            first_group.remove(first_group_arrow_down)
            first_group_arrow_down = CurvedArrow(start_point=first_group_rec.get_bottom(), end_point=counter_2_rec.get_top(), angle=PI/4, color=WHITE)
            first_group_arrow_down.tip.height = 0.3
            first_group.add(first_group_arrow_down)
            


            self.play(
                Create(counter_2_group_arrow),
                Create(first_group_arrow_down),
                Create(counter_3_group_arrow),
                first_group.animate.shift(LEFT*2),
                Create(second_group)
            )

            first_group_next_arrow = CurvedArrow(start_point=first_group_rec.get_right(), end_point=second_group_rec.get_left(), angle=-PI/2, color=WHITE)
            first_group_next_arrow.tip.height = 0.3
            first_group.add(first_group_next_arrow)

            second_group_prev_arrow = CurvedArrow(start_point=second_group_rec.get_left(), end_point=first_group_rec.get_right(), angle=-PI/2, color=WHITE)
            second_group_prev_arrow.tip.height = 0.3
            second_group.add(second_group_prev_arrow)

            self.play(Create(first_group_next_arrow), Create(second_group_prev_arrow))
            
            # second ball into counter
            ball_2 = self.make_stream_ball_2(STREAM[1])
            ball_2.generate_target()
            ball_2.target.move_to(counter_2_cross.get_center())
            self.play(MoveToTarget(ball_2))
            self.play(ReplacementTransform(counter_2_cross, ball_2))

            # moving second counter to second group
            counter_2.remove(counter_2_next_arrow, counter_2_group_arrow)
            counter_2.generate_target()
            counter_2.target.next_to(counter_1_rec, LEFT)

            counter_3.remove(counter_3_prev_arrow, counter_3_group_arrow)
            counter_3.shift(LEFT)
            counter_3_group_arrow = CurvedArrow(start_point=counter_3_rec.get_top(), end_point=first_group_rec.get_bottom(), angle=PI/2, color=WHITE)
            counter_3_group_arrow.tip.height = 0.3
            counter_3.add(counter_3_group_arrow)
            first_group.remove(first_group_arrow_down)
            first_group_arrow_down = CurvedArrow(start_point=first_group_rec.get_bottom(), end_point=counter_3_rec.get_top(), angle=PI/2, color=WHITE)
            first_group_arrow_down.tip.height = 0.3
            first_group.add(first_group_arrow_down)
            first_group.remove(counter_2)
            second_group.add(counter_2)

            self.play(
                MoveToTarget(counter_2),
                counter_1.animate.shift(RIGHT),
                Create(counter_3_group_arrow),
                Create(first_group_arrow_down),
                Uncreate(second_group_arrow_down),
                Uncreate(counter_1_group_arrow)
            )  


            second_group.remove(second_group_arrow_down)
            second_group_arrow_down = CurvedArrow(start_point=second_group_rec.get_bottom(), end_point=counter_2_rec.get_top(), angle=PI/4, color=WHITE)
            second_group_arrow_down.tip.height = 0.3
            second_group.add(second_group_arrow_down)
            counter_1.remove(counter_1_group_arrow)
            counter_1_group_arrow = CurvedArrow(start_point=counter_1_rec.get_top(), end_point=second_group_rec.get_bottom(), angle=0, color=WHITE)
            counter_1_group_arrow.tip.height = 0.3
            counter_1.add(counter_1_group_arrow)

            counter_2_group_arrow = CurvedArrow(start_point=counter_2_rec.get_top(), end_point=second_group_rec.get_bottom(), angle=PI/4, color=WHITE)
            counter_2_group_arrow.tip.height = 0.3
            counter_2.add(counter_2_group_arrow)

            counter_2_next_arrow = CurvedArrow(start_point=counter_2_rec.get_right(), end_point=counter_1_rec.get_left(), angle=-PI/2, color=WHITE)
            counter_2_next_arrow.tip.height = 0.3
            counter_2.add(counter_2_next_arrow)
            counter_1_prev_arrow = CurvedArrow(start_point=counter_1_rec.get_left(), end_point=counter_2_rec.get_right(), angle=-PI/2, color=WHITE)
            counter_1_prev_arrow.tip.height = 0.3
            counter_1.add(counter_1_prev_arrow)

            self.play(Create(second_group_arrow_down), Create(counter_1_group_arrow), Create(counter_2_next_arrow), Create(counter_1_prev_arrow))

            # third ball into counter
            ball_3 = self.make_stream_ball_2(STREAM[2])
            ball_3.generate_target()
            ball_3.target.move_to(counter_3_cross.get_center())
            self.play(MoveToTarget(ball_3))
            self.play(ReplacementTransform(counter_3_cross, ball_3))

            # moving third counter to second group
            counter_3.remove(counter_3_group_arrow)
            first_group.remove(counter_3)
            second_group.add(counter_3)
            second_group.remove(second_group_prev_arrow)

            self.play(
                Uncreate(first_group),
                Uncreate(second_group_prev_arrow),
                second_group.animate.shift(LEFT*2)
            )

            counter_2.remove(counter_2_group_arrow)
            counter_1.remove(counter_1_group_arrow)
            second_group.remove(second_group_arrow_down)
            second_group_text_2 = MathTex(r"\text{Value}=1")
            second_group_rec_2 = SurroundingRectangle(second_group_text_2, corner_radius=0.5, buff=0.5, color=WHITE)
            second_group_2 = VGroup(second_group_text_2, second_group_rec_2).scale(0.8)
            # second_group.remove(counter_1, counter_2, counter_3)
            second_group_2.add(counter_1, counter_2, counter_3)
            self.play(
                ReplacementTransform(second_group, second_group_2),
                Uncreate(counter_2_group_arrow),
                Uncreate(counter_1_group_arrow),
                Uncreate(second_group_arrow_down),
                counter_2.animate.shift(RIGHT*1.45),
                counter_1.animate.shift(RIGHT*1.45),
                counter_3.animate.shift(RIGHT*1.45),
            )
            counter_3_next_arrow = CurvedArrow(start_point=counter_3_rec.get_right(), end_point=counter_2_rec.get_left(), angle=-PI/2, color=WHITE)
            counter_3_next_arrow.tip.height = 0.3
            counter_3.add(counter_3_next_arrow)
            counter_2_prev_arrow = CurvedArrow(start_point=counter_2_rec.get_left(), end_point=counter_3_rec.get_right(), angle=-PI/2, color=WHITE)
            counter_2_prev_arrow.tip.height = 0.3
            counter_2.add(counter_2_prev_arrow)

            second_group_2_arrow_down = CurvedArrow(start_point=second_group_rec_2.get_critical_point(DL)+UP*0.1+RIGHT*0.1, end_point=counter_3_rec.get_top(), angle=0, color=WHITE)
            second_group_2_arrow_down.tip.height = 0.3
            second_group_2.add(second_group_2_arrow_down)


            counter_3_group_arrow = CurvedArrow(start_point=counter_3_rec.get_top(), end_point=second_group_rec_2.get_critical_point(DL)+UP*0.1+RIGHT*0.1, angle=-PI/2, color=WHITE)
            counter_3_group_arrow.tip.height = 0.3
            counter_3.add(counter_3_group_arrow)
            counter_2_group_arrow = CurvedArrow(start_point=counter_2_rec.get_top(), end_point=second_group_rec_2.get_bottom(), angle=0, color=WHITE)
            counter_2_group_arrow.tip.height = 0.3
            counter_2.add(counter_2_group_arrow)
            counter_1_group_arrow = CurvedArrow(start_point=counter_1_rec.get_top(), end_point=second_group_rec_2.get_critical_point(DR)+UP*0.1+LEFT*0.1, angle=PI/2, color=WHITE)
            counter_1_group_arrow.tip.height = 0.3
            counter_1.add(counter_1_group_arrow)

            self.play(
                Create(counter_3_group_arrow),
                Create(counter_2_group_arrow),
                Create(counter_1_group_arrow),
                Create(second_group_2_arrow_down),
                Create(counter_3_next_arrow),
                Create(counter_2_prev_arrow)
            )

            # fourth ball into counter
            ball_4 = self.make_stream_ball_2(STREAM[3])
            self.play(ReplacementTransform(ball_4, ball_1))

            self.wait(2)






        







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
    
    def contradiction_arrow(self):
        diag1 = Line(start=[1,1,0], end=[-1,-1,0], stroke_width=8)
        horiz = Line(start=[-1,-1,0], end=[1,-1,0], stroke_width=8)
        diag2 = Line(start=[1,-1,0], end=[0,-2,0], stroke_width=8)
        arrow = Arrow(start=[1,-1,0], end=[-1,-3,0], stroke_width=8)
        return VGroup(diag1, horiz, diag2, arrow).set_color(RED).shift(UP*0.5)
    
    def make_stream_ball_2(self,color):
        ball = Circle(radius=0.5, color=color, fill_opacity=1)
        ball.move_to([0,5,0])
        ball.generate_target()
        ball.target.move_to([0,3,0])
        self.play(Create(ball))
        self.play(MoveToTarget(ball))
        return ball
