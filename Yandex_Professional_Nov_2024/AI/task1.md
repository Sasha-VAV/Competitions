<div class="problem__statement text" data-bem="{&quot;problem__statement&quot;:{}}">
<div class="problem-statement"><div class="header"><h1 class="title">1. Фруктовая метрика (5)</h1><table></table></div><h2></h2><div class="legend"><p><em>Задача предоставлена Научно-образовательным центром когнитивного моделирования МФТИ</em></p> 
<p>Вы работаете в лаборатории, разрабатывающей алгоритм для автоматической сортировки плодов на <em><strong>Спелые</strong></em> и <em><strong>Неспелые</strong></em>. Алгоритм оценивает вероятность того, что плод является <em><strong>Спелым</strong></em>. Чтобы понять, насколько хорошо алгоритм справляется с задачей классификации, вам нужно рассчитать метрику <strong>Average Precision (AP)</strong>. Эта метрика поможет оценить точность предсказания модели для класса <em><strong>Спелый</strong></em> при различных порогах вероятности от 0 до 1 ([0, 1) с шагом 0.1).</p> 
<p><strong>Precision</strong> (точность) для бинарной классификации — это доля правильных положительных предсказаний среди всех предсказанных положительных классов. Формально, точность для порога <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-1-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-1" class="mjx-math"><span id="MJXc-Node-2" class="mjx-mrow"><span id="MJXc-Node-3" class="mjx-semantics"><span id="MJXc-Node-4" class="mjx-mrow"><span id="MJXc-Node-5" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">t</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-1"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        t
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       t
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6151em;"></span><span class="mord mathnormal">t</span></span></span></span></span> можно выразить как:</p> 
<p><span class="math display"><span class="katex-display"><span class="katex"><span class="katex-mathml">
     <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="mjx-chtml MJXc-display" style="text-align: center;"><span id="MathJax-Element-2-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%; text-align: center;"><span id="MJXc-Node-6" class="mjx-math"><span id="MJXc-Node-7" class="mjx-mrow"><span id="MJXc-Node-8" class="mjx-semantics"><span id="MJXc-Node-9" class="mjx-mrow"><span id="MJXc-Node-10" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-11" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">r</span></span><span id="MJXc-Node-12" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">e</span></span><span id="MJXc-Node-13" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">c</span></span><span id="MJXc-Node-14" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">i</span></span><span id="MJXc-Node-15" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">s</span></span><span id="MJXc-Node-16" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">i</span></span><span id="MJXc-Node-17" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">o</span></span><span id="MJXc-Node-18" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">n</span></span><span id="MJXc-Node-19" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">(</span></span><span id="MJXc-Node-20" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">t</span></span><span id="MJXc-Node-21" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">)</span></span><span id="MJXc-Node-22" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.076em; padding-bottom: 0.292em;">=</span></span><span id="MJXc-Node-23" class="mjx-mfrac MJXc-space3"><span class="mjx-box MJXc-stacked" style="width: 6.655em; padding: 0px 0.12em;"><span class="mjx-numerator" style="width: 6.655em; top: -1.585em;"><span id="MJXc-Node-24" class="mjx-mrow"><span id="MJXc-Node-25" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.12em;">T</span></span><span id="MJXc-Node-26" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-27" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">(</span></span><span id="MJXc-Node-28" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">t</span></span><span id="MJXc-Node-29" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">)</span></span></span></span><span class="mjx-denominator" style="width: 6.655em; bottom: -1.085em;"><span id="MJXc-Node-30" class="mjx-mrow"><span id="MJXc-Node-31" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.12em;">T</span></span><span id="MJXc-Node-32" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-33" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">(</span></span><span id="MJXc-Node-34" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">t</span></span><span id="MJXc-Node-35" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">)</span></span><span id="MJXc-Node-36" class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.292em; padding-bottom: 0.437em;">+</span></span><span id="MJXc-Node-37" class="mjx-mi MJXc-space2"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.106em;">F</span></span><span id="MJXc-Node-38" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-39" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">(</span></span><span id="MJXc-Node-40" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">t</span></span><span id="MJXc-Node-41" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">)</span></span></span></span><span class="mjx-line" style="border-bottom: 1.3px solid; top: -0.295em; width: 6.655em;"></span></span><span class="mjx-vsize" style="height: 2.671em; vertical-align: -1.085em;"></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-2"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
      <semantics>
       <mrow>
        <mi>
         P
        </mi>
        <mi>
         r
        </mi>
        <mi>
         e
        </mi>
        <mi>
         c
        </mi>
        <mi>
         i
        </mi>
        <mi>
         s
        </mi>
        <mi>
         i
        </mi>
        <mi>
         o
        </mi>
        <mi>
         n
        </mi>
        <mo stretchy="false">
         (
        </mo>
        <mi>
         t
        </mi>
        <mo stretchy="false">
         )
        </mo>
        <mo>
         =
        </mo>
        <mfrac>
         <mrow>
          <mi>
           T
          </mi>
          <mi>
           P
          </mi>
          <mo stretchy="false">
           (
          </mo>
          <mi>
           t
          </mi>
          <mo stretchy="false">
           )
          </mo>
         </mrow>
         <mrow>
          <mi>
           T
          </mi>
          <mi>
           P
          </mi>
          <mo stretchy="false">
           (
          </mo>
          <mi>
           t
          </mi>
          <mo stretchy="false">
           )
          </mo>
          <mo>
           +
          </mo>
          <mi>
           F
          </mi>
          <mi>
           P
          </mi>
          <mo stretchy="false">
           (
          </mo>
          <mi>
           t
          </mi>
          <mo stretchy="false">
           )
          </mo>
         </mrow>
        </mfrac>
       </mrow>
       <annotation encoding="application/x-tex">
        Precision(t) = \frac{TP(t)}{TP(t) + FP(t)}
       </annotation>
      </semantics>
     </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">P</span><span class="mord mathnormal">rec</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord mathnormal">i</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:2.363em;vertical-align:-0.936em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.427em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.13889em;">TP</span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">FP</span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mclose">)</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.677em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal" style="margin-right:0.13889em;">TP</span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mclose">)</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.936em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span></span></p> 
<p>где <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-3-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-42" class="mjx-math"><span id="MJXc-Node-43" class="mjx-mrow"><span id="MJXc-Node-44" class="mjx-semantics"><span id="MJXc-Node-45" class="mjx-mrow"><span id="MJXc-Node-46" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.12em;">T</span></span><span id="MJXc-Node-47" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-48" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-49" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">t</span></span><span id="MJXc-Node-50" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-3"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        T
       </mi>
       <mi>
        P
       </mi>
       <mo stretchy="false">
        (
       </mo>
       <mi>
        t
       </mi>
       <mo stretchy="false">
        )
       </mo>
      </mrow>
      <annotation encoding="application/x-tex">
       TP(t)
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">TP</span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mclose">)</span></span></span></span></span> — это количество истинных положительных предсказаний (плоды классифицированы как <em><strong>Спелые</strong></em> и действительно <em><strong>Спелые</strong></em>), а <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-4-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-51" class="mjx-math"><span id="MJXc-Node-52" class="mjx-mrow"><span id="MJXc-Node-53" class="mjx-semantics"><span id="MJXc-Node-54" class="mjx-mrow"><span id="MJXc-Node-55" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.106em;">F</span></span><span id="MJXc-Node-56" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-57" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-58" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">t</span></span><span id="MJXc-Node-59" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-4"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        F
       </mi>
       <mi>
        P
       </mi>
       <mo stretchy="false">
        (
       </mo>
       <mi>
        t
       </mi>
       <mo stretchy="false">
        )
       </mo>
      </mrow>
      <annotation encoding="application/x-tex">
       FP(t)
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">FP</span><span class="mopen">(</span><span class="mord mathnormal">t</span><span class="mclose">)</span></span></span></span></span> — это количество ложных положительных предсказаний (плоды классифицированы как <em><strong>Спелые</strong></em>, но на самом деле они <em><strong>Неспелые</strong></em>).</p> 
<p><strong>Average Precision (AP)</strong> рассчитывается как среднее значение точности для различных порогов вероятности:</p> 
<p><span class="math display"><span class="katex-display"><span class="katex"><span class="katex-mathml">
     <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="mjx-chtml MJXc-display" style="text-align: center;"><span id="MathJax-Element-5-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%; text-align: center;"><span id="MJXc-Node-60" class="mjx-math"><span id="MJXc-Node-61" class="mjx-mrow"><span id="MJXc-Node-62" class="mjx-semantics"><span id="MJXc-Node-63" class="mjx-mrow"><span id="MJXc-Node-64" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.509em; padding-bottom: 0.292em;">A</span></span><span id="MJXc-Node-65" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-66" class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.076em; padding-bottom: 0.292em;">=</span></span><span id="MJXc-Node-67" class="mjx-mfrac MJXc-space3"><span class="mjx-box MJXc-stacked" style="width: 0.8em; padding: 0px 0.12em;"><span class="mjx-numerator" style="width: 0.8em; top: -1.368em;"><span id="MJXc-Node-68" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.364em; padding-bottom: 0.364em;">1</span></span></span><span class="mjx-denominator" style="width: 0.8em; bottom: -0.722em;"><span id="MJXc-Node-69" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">n</span></span></span><span class="mjx-line" style="border-bottom: 1.3px solid; top: -0.295em; width: 0.8em;"></span></span><span class="mjx-vsize" style="height: 2.089em; vertical-align: -0.722em;"></span></span><span id="MJXc-Node-70" class="mjx-munderover MJXc-space1"><span class="mjx-itable"><span class="mjx-row"><span class="mjx-cell"><span class="mjx-stack"><span class="mjx-over" style="font-size: 70.7%; padding-bottom: 0.247em; padding-top: 0.141em; padding-left: 0.721em;"><span id="MJXc-Node-76" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.22em; padding-bottom: 0.292em;">n</span></span></span><span class="mjx-op"><span id="MJXc-Node-71" class="mjx-mo"><span class="mjx-char MJXc-TeX-size2-R" style="padding-top: 0.725em; padding-bottom: 0.725em;">∑</span></span></span></span></span></span><span class="mjx-row"><span class="mjx-under" style="font-size: 70.7%; padding-top: 0.236em; padding-bottom: 0.141em; padding-left: 0.21em;"><span id="MJXc-Node-72" class="mjx-mrow" style=""><span id="MJXc-Node-73" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">i</span></span><span id="MJXc-Node-74" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.076em; padding-bottom: 0.292em;">=</span></span><span id="MJXc-Node-75" class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.364em; padding-bottom: 0.364em;">1</span></span></span></span></span></span></span><span id="MJXc-Node-77" class="mjx-mtext MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.364em; padding-bottom: 0.364em;">Precision</span></span><span id="MJXc-Node-78" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">(</span></span><span id="MJXc-Node-79" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-80" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">t</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-81" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.437em; padding-bottom: 0.292em;">i</span></span></span></span><span id="MJXc-Node-82" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.437em; padding-bottom: 0.581em;">)</span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-5"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
      <semantics>
       <mrow>
        <mi>
         A
        </mi>
        <mi>
         P
        </mi>
        <mo>
         =
        </mo>
        <mfrac>
         <mn>
          1
         </mn>
         <mi>
          n
         </mi>
        </mfrac>
        <munderover>
         <mo>
          ∑
         </mo>
         <mrow>
          <mi>
           i
          </mi>
          <mo>
           =
          </mo>
          <mn>
           1
          </mn>
         </mrow>
         <mi>
          n
         </mi>
        </munderover>
        <mtext>
         Precision
        </mtext>
        <mo stretchy="false">
         (
        </mo>
        <msub>
         <mi>
          t
         </mi>
         <mi>
          i
         </mi>
        </msub>
        <mo stretchy="false">
         )
        </mo>
       </mrow>
       <annotation encoding="application/x-tex">
        AP = \frac{1}{n} \sum_{i=1}^{n} \text{Precision}(t_i)
       </annotation>
      </semantics>
     </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal">A</span><span class="mord mathnormal" style="margin-right:0.13889em;">P</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:2.9291em;vertical-align:-1.2777em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.3214em;"><span style="top:-2.314em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathnormal">n</span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.677em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.686em;"><span></span></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.6514em;"><span style="top:-1.8723em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">i</span><span class="mrel mtight">=</span><span class="mord mtight">1</span></span></span></span><span style="top:-3.05em;"><span class="pstrut" style="height:3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span><span style="top:-4.3em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathnormal mtight">n</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.2777em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord text"><span class="mord">Precision</span></span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span></span></p> 
<p>где <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-6-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-83" class="mjx-math"><span id="MJXc-Node-84" class="mjx-mrow"><span id="MJXc-Node-85" class="mjx-semantics"><span id="MJXc-Node-86" class="mjx-mrow"><span id="MJXc-Node-87" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-88" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">t</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-89" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-6"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         t
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       t_i
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7651em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> — это порог вероятности, а <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-7-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-90" class="mjx-math"><span id="MJXc-Node-91" class="mjx-mrow"><span id="MJXc-Node-92" class="mjx-semantics"><span id="MJXc-Node-93" class="mjx-mrow"><span id="MJXc-Node-94" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.48em; padding-bottom: 0.301em; padding-right: 0.109em;">P</span></span><span id="MJXc-Node-95" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">r</span></span><span id="MJXc-Node-96" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">e</span></span><span id="MJXc-Node-97" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">c</span></span><span id="MJXc-Node-98" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span><span id="MJXc-Node-99" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">s</span></span><span id="MJXc-Node-100" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span><span id="MJXc-Node-101" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">o</span></span><span id="MJXc-Node-102" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.241em; padding-bottom: 0.301em;">n</span></span><span id="MJXc-Node-103" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">(</span></span><span id="MJXc-Node-104" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-105" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">t</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-106" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span><span id="MJXc-Node-107" class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.48em; padding-bottom: 0.599em;">)</span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-7"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        P
       </mi>
       <mi>
        r
       </mi>
       <mi>
        e
       </mi>
       <mi>
        c
       </mi>
       <mi>
        i
       </mi>
       <mi>
        s
       </mi>
       <mi>
        i
       </mi>
       <mi>
        o
       </mi>
       <mi>
        n
       </mi>
       <mo stretchy="false">
        (
       </mo>
       <msub>
        <mi>
         t
        </mi>
        <mi>
         i
        </mi>
       </msub>
       <mo stretchy="false">
        )
       </mo>
      </mrow>
      <annotation encoding="application/x-tex">
       Precision(t_i)
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">P</span><span class="mord mathnormal">rec</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord mathnormal">i</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mopen">(</span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mclose">)</span></span></span></span></span> — точность для предсказаний, сделанных при данном пороге <span class="math inline"><span class="katex"><span class="katex-mathml">
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span id="MathJax-Element-8-Frame" class="mjx-chtml MathJax_CHTML" tabindex="0" style="font-size: 99%;"><span id="MJXc-Node-108" class="mjx-math"><span id="MJXc-Node-109" class="mjx-mrow"><span id="MJXc-Node-110" class="mjx-semantics"><span id="MJXc-Node-111" class="mjx-mrow"><span id="MJXc-Node-112" class="mjx-msub"><span class="mjx-base"><span id="MJXc-Node-113" class="mjx-mi"><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">t</span></span></span><span class="mjx-sub" style="font-size: 70.7%; vertical-align: -0.212em; padding-right: 0.071em;"><span id="MJXc-Node-114" class="mjx-mi" style=""><span class="mjx-char MJXc-TeX-math-I" style="padding-top: 0.42em; padding-bottom: 0.301em;">i</span></span></span></span></span></span></span></span></span><script type="math/mml" id="MathJax-Element-8"><math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         t
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       t_i
      </annotation>
     </semantics>
    </math></script></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7651em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>Массив вероятностей и истинных меток представлен в таблице:</p> 
<pre><code>| № Фотографии | Вероятность предсказания | Истинная метка |
| ------------ | ------------------------ | -------------- |
| 1            | 0.85                     | Спелый         |
| 2            | 0.55                     | Спелый         |
| 3            | 0.65                     | Неспелый       |
| 4            | 0.40                     | Спелый         |
| 5            | 0.95                     | Спелый         |
| 6            | 0.75                     | Неспелый       |
| 7            | 0.50                     | Спелый         |
| 8            | 0.60                     | Спелый         |
| 9            | 0.30                     | Неспелый       |
| 10           | 0.80                     | Спелый         |</code></pre></div><h2>Формат вывода</h2><div class="output-specification"><p>Вам необходимо написать значение посчитанного <strong>Average Precision</strong>, записанное через запятую (или точку) и округленное до двух знаков после запятой (точки).</p></div><h2>Примечания</h2><div class="notes"><p>При пороге, например, 0.1 предсказание с вероятностью 0.1 считается <em><strong>Спелым</strong></em>.</p></div></div></div>